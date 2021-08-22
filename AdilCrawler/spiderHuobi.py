import asyncio
import websockets

# # 向服务器端认证，用户名密码通过才能退出循环
# async def auth_system(websocket):
#     while True:
#         cred_text = input("please enter your username and password: ")
#         await websocket.send(cred_text)
#         response_str = await websocket.recv()
#         if "congratulation" in response_str:
#             return True
#
# # 向服务器端发送认证后的消息
# async def send_msg(websocket):
#     while True:
#         _text = input("please enter your context: ")
#         if _text == "exit":
#             print(f'you have enter "exit", goodbye')
#             await websocket.close(reason="user exit")
#             return False
#         await websocket.send(_text)
#         recv_text = await websocket.recv()
#         print(f"{recv_text}")
#
# # 客户端主逻辑
# async def main_logic():
#     async with websockets.connect('ws://10.10.6.91:5678') as websocket:
#         await auth_system(websocket)
#
#         await send_msg(websocket)
#
# asyncio.get_event_loop().run_until_complete(main_logic())

import sys,threading
# from threading import thread
try:
      import websocket
except ImportError:
      print("请先安装websocket-client-py3扩展")
      sys.exit(1)


# class socket:
#       """
#       socket通讯
#       """
#       address = "ws://127.0.0.1:2345"
#       ws = None
#
#       def __init__(self):
#             websocket.enableTrace(False)
#             self.ws = websocket.WebSocketApp(self.address,
#                                              on_message=self.on_message,
#                                              on_error=self.on_error,
#                                              on_close=self.on_close,
#                                              on_open=self.on_open)
#             self.ws.run_forever()
#
#       def on_message(self, ws, message):
#             """
#             服务端消息
#             :param ws:
#             :param message:
#             :return:
#             """
#             print(message)
#
#       def on_error(self, ws, error):
#             print("错误：" + error)
#
#       def on_close(self, ws):
#             print("### closed ###")
#
#       def on_open(self, ws):
#             def run(*args):
#                   ws.send('hello')
#                   print("thread terminating...")
#
#             # thread.start_new_thread(run, ())


#
# import ssl
# from websocket import create_connection
#
# ws = create_connection("wss://www.huobi.bo/-/s/pro/ws", timeout=5, sslopt={"cert_reqs": ssl.CERT_NONE})
# if ws.connected:
#       # ws.send('8')
#       print(ws.recv())
#       # ws.close()

import websocket
from threading import Thread
import time



# if __name__ == "__main__":
#       websocket.enableTrace(True)
#       ws = websocket.WebSocketApp("ws://echo.websocket.org/",
#                                   on_message=on_message,
#                                   on_error=on_error,
#                                   on_close=on_close)
#       ws.on_open = on_open
#       ws.run_forever()



import websocket
import ssl
import gzip
import time
import datetime
import json
import demjson

def on_message(ws, message):  # 服务器有数据更新时，主动推送过来的数据
    print("message=", message)
    ret = gzip.decompress(message).decode("utf-8")
    if ('ping' in ret):
        return
    text = demjson.decode(ret)
    print('=------', text)
    for index in range(len(text['tick']['data'])):
        print('ds='+str(text['tick']['data'][index]['ds']))
        print('price='+str(text['tick']['data'][index]['price']))
        print('side='+str(text['tick']['data'][index]['side']))
        print('vol='+str(text['tick']['data'][index]['vol']))
        print('###################分割线#############################')
    # print(text.keys())
    # print('amount='+str(text['tick']['data'][0]['amount']) )
    # print('ds='+str(text['tick']['data'][0]['ds']))
    # print('id='+str(text['tick']['data'][0]['id']))
    # print('price='+str(text['tick']['data'][0]['price']))
    # print('side='+str(text['tick']['data'][0]['side']))
    # print('ts='+str(text['tick']['data'][0]['ts']))
    # print('vol='+str(text['tick']['data'][0]['vol']))

# 程序报错时，就会触发on_error事件
def on_error(ws, error):
    print("error=", error)

# 程序关闭后触发close时间
def on_close(ws):
    print("Connection closed ……")

# 连接到服务器之后就会触发on_open事件
def on_open(ws):
    # ws.send('{"event":"req","params":{"channel":"review"}}') #获取review数据
    # 获取btcusdt
    ws.send('{"event": "sub", "params": {"channel": "market_btcusdt_trade_ticker", "cb_id": "btcusdt", "top": 100}}')




if __name__ == "__main__":
    ck = "_ga=GA1.2.1242066176.1629033378; _gid=GA1.2.1702130203.1629033378; __zlcmid=15akG0HrGrWjjmL; HB_SSO=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-UC-TOKEN=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-PRO-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; hbsession=a10ad55b-5f25-44e7-aa23-49fb49c3fa29; token=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; HB-OLD-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22A743263FC0B0620292D52C402548777723B39ABDBE449CAC5B368412D17AAA41%22%2C%22first_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%7D; _ha_session=1629174520691; _ha_session_id=6f239d75-c32a-3fe5-bf8b-da9f420f; etpToTradeTip=1"
    websocket.enableTrace(True)
    wss_url = "wss://www.huobi.bo/-/s/pro/ws/v2"

    a = "wss://wspool.mpuuss.top/kline-api/ws"
    """
    Host: www.huobi.bo
Connection: Upgrade
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
Upgrade: websocket
Origin: https://www.huobi.bo
Sec-WebSocket-Version: 13
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: _ga=GA1.2.1242066176.1629033378; _gid=GA1.2.1702130203.1629033378; __zlcmid=15akG0HrGrWjjmL; HB_SSO=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-UC-TOKEN=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-PRO-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; hbsession=a10ad55b-5f25-44e7-aa23-49fb49c3fa29; token=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; HB-OLD-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22A743263FC0B0620292D52C402548777723B39ABDBE449CAC5B368412D17AAA41%22%2C%22first_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%7D; _ha_session=1629174520691; _ha_session_id=6f239d75-c32a-3fe5-bf8b-da9f420f; etpToTradeTip=1
Sec-WebSocket-Key: +F0lGMc5+TslxsEI2vxN9A==
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
    """

    ab = """
    Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: Upgrade
Cookie: _ga=GA1.2.1242066176.1629033378; _gid=GA1.2.1702130203.1629033378; __zlcmid=15akG0HrGrWjjmL; HB_SSO=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-UC-TOKEN=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-PRO-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; hbsession=a10ad55b-5f25-44e7-aa23-49fb49c3fa29; token=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; HB-OLD-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22A743263FC0B0620292D52C402548777723B39ABDBE449CAC5B368412D17AAA41%22%2C%22first_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%7D; _ha_session=1629262300244; _ha_session_id=2d4f74de-3b63-33a5-be4b-ddf916b3
Host: www.huobi.bo
Origin: https://www.huobi.bo
Pragma: no-cache
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
Sec-WebSocket-Key: THTHw3+pcwrE2ud6NgwgVA==
Sec-WebSocket-Version: 13
Upgrade: websocket
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
    
    """

    header1 = [
                                        "Host: www.huobi.bo",
                                        "Connection: Upgrade ",
                                        "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 ",
                                         "Cache-Control: no-cache",
                                        "Origin: https://www.huobi.bo",
                                        "Sec-WebSocket-Version: 13 ",
                                        "Sec-WebSocket-Key: +F0lGMc5+TslxsEI2vxN9A==",
                                        "Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits"
                                        "Cookie: _ga=GA1.2.1242066176.1629033378; _gid=GA1.2.1702130203.1629033378; __zlcmid=15akG0HrGrWjjmL; HB_SSO=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-UC-TOKEN=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-PRO-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; hbsession=a10ad55b-5f25-44e7-aa23-49fb49c3fa29; token=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; HB-OLD-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22A743263FC0B0620292D52C402548777723B39ABDBE449CAC5B368412D17AAA41%22%2C%22first_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%7D; _ha_session=1629174520691; _ha_session_id=6f239d75-c32a-3fe5-bf8b-da9f420f; etpToTradeTip=1"
                                             ]


    header2 = [
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: zh-CN,zh;q=0.9",
        "Cache-Control: no-cache",
        "Connection: Upgrade",
        "Cookie: _ga=GA1.2.1242066176.1629033378; _gid=GA1.2.1702130203.1629033378; __zlcmid=15akG0HrGrWjjmL; HB_SSO=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-UC-TOKEN=oFDVU0fopFf73Z8QQNDguyyNJ8aX0AFK0jmVCqFTnBAajmWazyZHnwpYH3f5mlqf9dpPXHHfso6sBzDZgu8DQv1YUin0M4Wl2gsUFHkzh7SgIuGT3hHuiHcqgyWxVt5Q5OCpZ2WJi6HFHzg4LzZoSZjGtzs5aAlD5UCJzQKAGvYdtU/NBRkTY1rgX2T7x4O+CZ2hbQ7QymWkYkVSed9W2A==; HB-PRO-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; hbsession=a10ad55b-5f25-44e7-aa23-49fb49c3fa29; token=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; HB-OLD-TOKEN=dWMzoKi96dUH7IM_0ISruztB55NfVXE9sPOwHt3xFBUY-uOP2m0-gvjE57ad1qDF; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22A743263FC0B0620292D52C402548777723B39ABDBE449CAC5B368412D17AAA41%22%2C%22first_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217b49f494fa436-0005f8463bb2be55-30647c00-1296000-17b49f494fb617%22%7D; _ha_session=1629262300244; _ha_session_id=2d4f74de-3b63-33a5-be4b-ddf916b3",

        "Host: www.huobi.bo",
        "Origin: https://www.huobi.bo",
        "Pragma: no-cache",
        "Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits",
        "Sec-WebSocket-Key: THTHw3+pcwrE2ud6NgwgVA==",
        "Sec-WebSocket-Version: 13",
        "Upgrade: websocket",
        "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    ]


    ws = websocket.WebSocketApp(wss_url,
                                header= header2,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                               )
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    # ws.run_forever()



