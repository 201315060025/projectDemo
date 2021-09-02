# encoding: utf-8
"""
此方法完成的是多线程文件中写数据 1-100
"""

from threading import Thread, Lock, Semaphore
import time


lk = Lock()
se = Semaphore(5)
def write_file(num):
    # lk.acquire()lk.release()
    se.acquire()
    with open("wirte.txt", "a+") as w:
        w.write(str(num)+"\n")
    se.release()

# 测试方法
# write_file(1)
# write_file(2)
# write_file(3)


def normal_fun():
    # 1-100数字 使用多线程写入
    num_list = list(range(1, 101))
    # five_time = [num for num in  num_list if num % 5==0]
    sep = 5
    five_time = [num_list[i:i + sep] for i in range(0, len(num_list), sep)]
    # print("five_time", five_time)
    for ff in five_time:
        # print(ff)
        if len(ff) != 5:
            continue
        t1 = Thread(target=write_file, args=(ff[0],))
        t2 = Thread(target=write_file, args=(ff[1],))
        t3 = Thread(target=write_file, args=(ff[2],))

        t4 = Thread(target=write_file, args=(ff[3],))
        t5 = Thread(target=write_file, args=(ff[4],))

        t1.start()
        t2.start()
        t3.start()

        t4.start()
        t5.start()
        # break

normal_fun()