import asyncio, json, pickle, os
import logging
import time
from datetime import datetime
from aiowebsocket.converses import AioWebSocket
import gzip
from senMessageTool import SendMessageTool
from config import currency_cate


def handle(current_data, currency_data):
    buy_price = float(currency_data['buy_in_price'])
    new_price = float(current_data['close'])
    flag = (new_price - buy_price) / buy_price
    return flag > 0.9


def cal_time(start_time:str, end_time:str)->str:
    st = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    ed = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    return str((ed-st).days)


async def day_execute(uri,  parame):
    current_day = ""
    while True:
        new_day = datetime.now().strftime('%Y-%m-%d')
        if len(current_day) == 0 or new_day != current_day:
            current_day_message = []
            for currency_data in parame:
                ct = currency_data['currency'].replace('_', '')
                async with AioWebSocket(uri) as aws:
                    converse = aws.manipulator
                    message = '{"sub":"market.' + ct + '.kline.1min","symbol":"' + ct + '", "id": "id1"}'
                    while True:
                        await converse.send(message)
                        mes = await converse.receive()
                        mes1 = gzip.decompress(mes).decode("utf-8")
                        res = json.loads(mes1)
                        if "tick" in res:
                            break

                    name = currency_data["currency"].split('_')[0]
                    newPrice = res['tick']['close']
                    buy_price = float(currency_data['buy_in_price'])
                    rate = str(round((newPrice - buy_price) / buy_price, 3))
                    hold_money = currency_data['total_money']
                    hold_time = cal_time(currency_data['start_time'], new_day + " 00:00:00")
                    # name, 买入金额, 持有时间, 买入价, 当前价格, 增常率
                    message = [f"{name},{hold_money}, {hold_time}, {str(buy_price)},{str(newPrice)}, {rate}"]
                    current_day_message.extend(message)
            current_day = new_day
            # 只发邮箱
            SendMessageTool.send_message_by_email(current_day_message)
            # 同时保存一个记录

            if os.path.exists('data.pkl'):
                with open('data.pkl', 'rb') as ff:
                    data = pickle.load(ff)
            else:
                data = {}

            data.update({
                new_day: current_day_message
            })
            with open('data.pkl', 'wb') as ff:
                pickle.dump(data, ff)


async def startup(uri, ct, parame):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        # 最近24小时成交量、成交额、开盘价、收盘价、最高价、最低价、成交笔数等
        message = '{"sub":"market.' + ct + '.kline.1min","symbol":"' + ct + '", "id": "id1"}'
        count = 0
        while True:
            await converse.send(message)
            # print('{time}-Client send: {message}'
            #       .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message=message))
            mes = await converse.receive()
            mes1 = gzip.decompress(mes).decode("utf-8")
            res = json.loads(mes1)
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if "tick" not in res:
                # 请求开始 没有数据
                continue

            # 判断是否发短信
            if handle(res['tick'], parame) and count == 0:
                # 已经大雨30¥ 可以考虑卖出
                name = parame["currency"].split('_')[0]
                newPrice = res['tick']['close']
                buy_price = float(parame['buy_in_price'])
                rate = str(round((newPrice - buy_price) / buy_price, 3))
                send_message = [f"{name}, {str(buy_price)}, {str(newPrice)}, {rate}"]
                # 同时邮箱发送和 短信发送
                SendMessageTool.send_message_by_email(send_message)
                SendMessageTool.send_message_by_sms(send_message)
                count += 1
                print(f'{parame["currency"]} 已经达到了增常率， 可以考虑出手')

            await asyncio.sleep(1)

async def get_data_from_huobi():
    print('12')
    remote = 'wss://www.huobi.do/-/s/pro/ws'
    try:
        # task1 = asyncio.create_task(startup(remote, ct, parame))
        gather_list = []
        # 1: 监控每个币种的实时价格
        for currency_data in currency_cate:
            gather_list.append(
                startup(remote, currency_data['currency'].replace('_', ''), currency_data)
            )
        # 2： 统计每个币种每天的变化趋势
        gather_list.append(day_execute(remote, currency_cate))
        await asyncio.gather(*gather_list)
    except KeyboardInterrupt as exc:
        logging.info('Quit.')
    # pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_data_from_huobi())
    # asyncio.run(get_data_from_huobi())