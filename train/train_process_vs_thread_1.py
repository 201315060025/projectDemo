# encoding： utf-8
"""
1: 测试IO操作， 多进程和多线程的IO操作那个效率高
    测试方案： 同时对文件， 在内存中操作后， 然后再写入到本地
"""
import time
import os
import json
import requests
import threading
import pandas as pd

import multiprocessing
thread_result = {}

def decorator_func(func):
    def wrapped():
        t1 = time.time()
        #print("start_time is", t1)
        func()
        #print("end is", time.time())
        print("hao shi", time.time()-t1)
    return wrapped


def read_and_write(source_file, target_file, thread_name):
    """
    单纯的运算， 没有任何的逻辑
    多进程：6.2624266147613525
    多线程：6.005255699157715
    :param source_file:
    :param target_file:
    :param thread_name:
    :return:
    """
    time.sleep(2)
    thread_result.update({thread_name: True})
    return True

def read_and_write2(source_file, target_file, thread_name):
    """
    IO操作
    多进程：1.4520320892333984
    多线程：0.009006261825561523
    :param source_file:
    :param target_file:
    :param thread_name:
    :return:
    """
    with open(source_file, "r") as f:
        # read 以字符串的形式 全部独处来
        # readline 读取文件的第一行
        # readlines 按行读取全部内容， 每一行代表list中的一个袁术
        data = f.read()

    with open(target_file, "w") as f:
        f.write(data)
    return True

def read_and_write3(source_file, target_file, thread_name):
    header = {
        "Cookie": "aliyungf_tc=AQAAAKYGpGBagwIAHpcnatTh27QXQwE3; acw_tc=2760822c15949955761788445ed9512e17ff1e3c4f4ad93eca28441a43463b; xq_a_token=ad923af9f68bb6a13ada0962232589cea11925c4; xqat=ad923af9f68bb6a13ada0962232589cea11925c4; xq_r_token=cf0e6f767c2318f1f1779fcee9323365f02e1b4b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU5NjE2MjgxNSwiY3RtIjoxNTk0OTk1NTMzMjE0LCJjaWQiOiJkOWQwbjRBWnVwIn0.Tsn5xZKtsEcHnfcWrp1GArrRUh12eSZw0lNztFQkV16HWf0ImxtIVSwZaVjzy-vq8eYe1_jdIXG_c9SL6uN2ar8yEbRX0_AZk71jFrMWCewI070UI0zTx7Nr4BUSunNrLh_vRDXb6lI945DLPEYsfmO8lMPxvcCu4GTLW_Us2qFct9QNc813i7hDVJeQiIz4tCuCjSBUl4tmfKtG61aPvG1JGKnHQNOod1YNqOzrGynDO9nQ6JWGCDAfYaE6NDZpM8iyx7zA8J9FWRD_FwSelan4XXO4Rm0qEGurcZAOkTSZCD95cPpyPDVKXxtUTWr6fz64VUoA16x_cOPwKLHm5w; u=241594995576182; device_id=24700f9f1986800ab4fcc880530dd0ed; s=dh117xl3cg; __utma=1.86557327.1594995482.1594995482.1594995482.1; __utmc=1; __utmz=1.1594995482.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1594995480,1594995563; __utmb=1.3.10.1594995482; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1594995572",
        "Host": "xueqiu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"

    }
    url = "https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=30&order=desc&order_by=percent&exchange=CN&market=CN&type=kcb&_=1594995592244%20Request%20Method:%20GET%20Status%20Code:%20200%20OK%20Remote%20Address:%20203.107.32.83:443%20Referrer%20Policy:%20unsafe-url%20Cache-Control:%20private,%20no-store,%20no-cache,%20must-revalidate,%20max-age=0%20Connection:%20keep-alive%20Content-Encoding:%20gzip%20Content-Type:%20application/json;%20charset=utf-8%20Date:%20Fri,%2017%20Jul%202020%2014:21:37%20GMT%20P3P:%20%22CP=%22IDC%20DSP%20COR%20ADM%20DEVi%20TAIi%20PSA%20PSD%20IVAi%20IVDi%20CONi%20HIS%20OUR%20IND%20CNT%22%22%20Server:%20openresty%20Strict-Transport-Security:%20max-age=31536000%20Transfer-Encoding:%20chunked%20Vary:%20Accept-Encoding%20X-Powered-By:%20Express%20X-RT:%2016%20Accept:%20*/*%20Accept-Encoding:%20gzip,%20deflate,%20br%20Accept-Language:%20zh-CN,zh;q=0.9%20cache-control:%20no-cache%20Connection:%20keep-alive%20Cookie:%20aliyungf_tc=AQAAAKYGpGBagwIAHpcnatTh27QXQwE3;%20acw_tc=2760822c15949955761788445ed9512e17ff1e3c4f4ad93eca28441a43463b;%20xq_a_token=ad923af9f68bb6a13ada0962232589cea11925c4;%20xqat=ad923af9f68bb6a13ada0962232589cea11925c4;%20xq_r_token=cf0e6f767c2318f1f1779fcee9323365f02e1b4b;%20xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU5NjE2MjgxNSwiY3RtIjoxNTk0OTk1NTMzMjE0LCJjaWQiOiJkOWQwbjRBWnVwIn0.Tsn5xZKtsEcHnfcWrp1GArrRUh12eSZw0lNztFQkV16HWf0ImxtIVSwZaVjzy-vq8eYe1_jdIXG_c9SL6uN2ar8yEbRX0_AZk71jFrMWCewI070UI0zTx7Nr4BUSunNrLh_vRDXb6lI945DLPEYsfmO8lMPxvcCu4GTLW_Us2qFct9QNc813i7hDVJeQiIz4tCuCjSBUl4tmfKtG61aPvG1JGKnHQNOod1YNqOzrGynDO9nQ6JWGCDAfYaE6NDZpM8iyx7zA8J9FWRD_FwSelan4XXO4Rm0qEGurcZAOkTSZCD95cPpyPDVKXxtUTWr6fz64VUoA16x_cOPwKLHm5w;%20u=241594995576182;%20device_id=24700f9f1986800ab4fcc880530dd0ed;%20s=dh117xl3cg;%20__utma=1.86557327.1594995482.1594995482.1594995482.1;%20__utmc=1;%20__utmz=1.1594995482.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);%20__utmt=1;%20Hm_lvt_1db88642e346389874251b5a1eded6e3=1594995480,1594995563;%20__utmb=1.3.10.1594995482;%20Hm_lpvt_1db88642e346389874251b5a1eded6e3=1594995572%20Host:%20xueqiu.com%20Referer:%20https://xueqiu.com/hq%20Sec-Fetch-Dest:%20empty%20Sec-Fetch-Mode:%20cors%20Sec-Fetch-Site:%20same-origin%20User-Agent:%20Mozilla/5.0%20(Windows%20NT%206.3;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/83.0.4103.116%20Safari/537.36%20X-Requested-With:%20XMLHttpRequest%20page:%201%20size:%2030%20order:%20desc%20order_by:%20percent%20exchange:%20CN%20market:%20CN%20type:%20kcb%20_:%201594995592244"
    response = requests.get(url, headers=header)
    data = json.loads(response.text)
    print(data["data"]["list"])
    df = pd.DataFrame(data["data"]["list"])
    df.to_csv(target_file, index=False)

def get_dir():
    source_dir, target_dir = r"C:\Users\pc\Desktop\test1", r"C:\Users\pc\Desktop\result1"
    file_list = os.listdir(source_dir)
    return [os.path.join(source_dir, ff) for ff in file_list], [os.path.join(target_dir, ff) for ff in file_list]

@decorator_func
def train_thread():
    source_file, target_file = get_dir()
    thread_list = []
    # 只允许有三个线程
    for idx, s_f in enumerate(source_file):
        t = threading.Thread(target=read_and_write3, args=(s_f, target_file[idx], "thread %d" % idx))
        t.name = "thread %d" % idx
        t.start()

        print(t.name+"start")
        thread_list.append(t)
        if len(thread_list) == 3:
            for thread_obj in thread_list:
                thread_obj.join()
                print("{0} thread result is {1}".format(thread_obj.name, thread_result.get(thread_obj.name, None)))
            thread_list.clear()

    if thread_list:
        for thread_obj in thread_list:
            thread_obj.join()
            print("{0} thread result is {1}".format(thread_obj.name, thread_result.get(thread_obj.name, None)))
        thread_list.clear()


        pass

#train_thread()
#print(thread_result)
@decorator_func
def train_process():
    source_file, target_file = get_dir()
    multi_exe = multiprocessing.Pool(processes=3)
    process_list = []
    for idx, ff in enumerate(source_file):
        # multi_exe.apply_async(read_and_write, (ff, target_file[idx],"process %d"%idx,))
        process_list.append(multi_exe.apply_async(read_and_write3, (ff, target_file[idx],"process %d"%idx,)))
    multi_exe.close()
    multi_exe.join()
    for s_f, res in zip(source_file, process_list):
        print(s_f, res.get(), time.time())

if __name__ == "__main__":
    print("多进程")
    train_process()
    print("\n"*2)
    print("多线程")
    # train_thread()
