# encoding: utf-8
"""
对比 在IO密集型 cpu密集型  网络请求密集型 不同类别下耗时对比
IO 密集型适合多线程，IO柱塞等待的空闲时间可以执行其他线程
"""
import requests
import time
from threading import Thread
from multiprocessing import Process


def count(x, y):
    """
    cpum密集型（计算）
    """
    # 使程序完成150万计算
    c = 0
    while c < 500000:
        c += 1
        x += x
        y += y


def write_and_read():
    """
    IO 密集型 write read
    :return:
    """
    f = open("test.txt", "w")
    for x in range(5000000):
        f.write("testwrite\n")
    f.close()

    f = open("test.txt", "r")
    lines = f.readlines()
    f.close()


def internet_requst():
    """
    定义网络请求函数
    :return:
    """
    _head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    url = "http://www.tieba.com"

    try:
        webPage = requests.get(url, headers=_head)
        html = webPage.text
        return {"context": html}
    except Exception as e:
        return {"error": e}




def line_exe():
    # CPU密集操作
    t = time.time()
    for x in range(10):
        count(1, 1)
    print("Line cpu", time.time() - t)

    # IO密集操作
    t = time.time()
    for x in range(10):
        write_and_read()
    print("Line IO", time.time() - t)

    # 网络请求密集型操作
    t = time.time()
    for x in range(10):
        internet_requst()
    print("Line Http Request", time.time() - t)


def mul_thread():
    # cpu
    counts = []
    t_cpu = time.time()
    for i in range(10):
        t = Thread(target=count, args=(1,2))
        t.start()
        counts.append(t)

    e =  counts.__len__()
    while True:
        for ct in counts:
            if not ct.is_alive():
                e -=1
            if e<=0:
                break
    print("mul thread cpu", time.time()-t_cpu)

    # IO 操作
    ios = []
    t_ios = time.time()
    for i in range(10):
        t_io = Thread(target=write_and_read)
        t_io.start()
        ios.append(t_io)

    for ios_obj in ios:
        ios_obj.join()
    print("mul thread IO", time.time()-t_ios)

    # internet requests
    inter_list = []
    t_inter = time.time()
    for i in range(10):
        t_inter = Thread(target=internet_requst)
        t_inter.start()
        inter_list.append(t_inter)
    for inter in inter_list:
        inter.join()
    print("mul thread inter", time.time()-t_inter)


def train_cpu():
    # cpu 密集型操作 实用
    # 线性执行
    t1 = time.time()
    count(1,2)
    print("line cpu", time.time()-t1)
    # 线程操作
    t_cpu_list = list()
    cpu_time = time.time()
    for i in range(10):
        t = Thread(target=count, args=(1, 1, ))
        t.start()
        t_cpu_list.append(t)

    for t_c in t_cpu_list:
        t_c.join()
    print("thread cpu", time.time()-cpu_time)
    # 多进程操作
    pro_cpu_list = list()
    t_pro_time = time.time()
    for i in range(10):
        p = Process(target=count, args=(1,1,))
        p.start()
        pro_cpu_list.append(p)
    for p_c in pro_cpu_list:
        p_c.join()
    print("process cpu", time.time()-t_pro_time)


def train_io():
     # IO 密集型操作 实用
    # 线性执行
    t1 = time.time()
    write_and_read()
    print("line io", time.time()-t1)
    # 线程操作
    t_cpu_list = list()
    cpu_time = time.time()
    for i in range(10):
        t = Thread(target=write_and_read)
        t.start()
        t_cpu_list.append(t)

    e =  t_cpu_list.__len__()
    while True:
        for ct in t_cpu_list:
            if not ct.is_alive():
                e -=1
            if e<=0:
                break

    for t_c in t_cpu_list:
        t_c.join()
    print("thread IO", time.time()-cpu_time)
    # 多进程操作
    pro_cpu_list = list()
    t_pro_time = time.time()
    for i in range(10):
        p = Process(target=write_and_read)
        p.start()
        pro_cpu_list.append(p)

    e =  pro_cpu_list.__len__()
    while True:
        for ct in pro_cpu_list:
            if not ct.is_alive():
                e -=1
            if e<=0:
                break
    # for p_c in pro_cpu_list:
    #     p_c.join()
    print("process IO", time.time()-t_pro_time)
    pass

if __name__ == "__main__":
    print("单线程操作")
    # line_exe()
    print("\n"*2)
    print("使用多线哼测试 cpu, io, 网络请求")
    #mul_thread()
    print("\n"*2)
    print("cpu 密集型下的线性， 线程 进程")
    #train_cpu()
    print("\n"*2)
    print("IO 密集型下的线性， 线程 进程")
    train_cpu()
