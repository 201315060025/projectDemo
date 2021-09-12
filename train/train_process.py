# encoding: utf-8
"""
多进程demo
   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
apply_async
apply()

close
join()  在条用join之前必须调用close ; 执行close后不再有新的进程加入pool, join() 函数等待所有的子进程执行完毕
"""

import multiprocessing
import time

def process_func(name, tt=0):
    print("{0} hello {1} start".format(str(time.time()),name))
    time.sleep(tt)
    print("{0} hello {1} end".format(str(time.time()),name))


def process_func_res(name, tt=0):
    print("{0} hello {1} start".format(str(time.time()),name))
    time.sleep(tt)
    print("{0} hello {1} end".format(str(time.time()),name))
    return name

def process_func_map(args):
    print("{0} hello {1} start".format(str(time.time()),args[0]))
    time.sleep(args[1])
    print("{0} hello {1} end".format(str(time.time()),args[0]))


def train1():
    """
    多进程 进程池 apply_async()
    :return:
    """
    mul_process = multiprocessing.Pool(processes = 3)
    for i in range(1,4):
        mul_process.apply_async(process_func, ("process_"+str(i), 3,))
    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    mul_process.close()
    mul_process.join()
    print("Sub-process(es) done.")

def train2():
    """
    多进程 进程池  apply
    :return:
    """
    mul_process = multiprocessing.Pool(processes=4)
    for ii in range(4):
        mul_process.apply(process_func, args=("process_%d"%ii, 3))
    print("aaa")
    mul_process.close()
    mul_process.join()
    print("process end..")

def train3():
    """
    多进程  进程池  并且关注结果
    :return:
    """
    mul_process = multiprocessing.Pool(processes=4)
    process_list = []
    for i in range(4):
        # 此处的mul_process
        # 如果用apply_async  获取结果 res.get()
        # 如果用apply      获取结果直接用 res
        process_list.append(mul_process.apply_async(process_func_res, ("process_%d"%i, 3)))
    mul_process.close()
    mul_process.join()
    print("process end.")

    for process_res in process_list:
        print(process_res.get())
        # print(process_res)


def train4():
    """
    多进程 进程池  map
    :return:
    """
    mul_process = multiprocessing.Pool(processes=4)
    process_name = [["thread%d"% i,2] for i in range(4)]

    # mul_process.map(process_func_map, process_name)
    mul_process.map_async(process_func_map, process_name)


def fun_sleep():
    time.sleep(6)
    print(aa)


if __name__ == "__main__":
    print("多进程 进程池 apply_async")
    t1 = time.time()
    # train1()
    t2 = time.time()
    print("apply_async need time is=", t2-t1)
    print("\n"*2)
    print("多进程 进程池 apply")
    # train2()
    t3 = time.time()
    print("apply need time is=", t3-t2)
    print("\n"*2)
    print("多进程 进程池 关注结果")

    # train3()
    t4 = time.time()
    print("get res need time is=", t4-t3)
    print("\n"*2)
    print("多进程 进程池 map")
    train4()

    # 进程监控
    p1 = multiprocessing.Process(target=fun_sleep, args=(), name='test_sleep')
    p1.start()
    print(id(p1))
    while True:
        print(p1.name, p1.is_alive())
        time.sleep(1)

        if p1.is_alive() == False:
            p1.terminate()
            print("p1 已经结束 重新开始")
            p1 = multiprocessing.Process(target=fun_sleep, args=(), name='test_sleep')
            print(id(p1))
            p1.start()

            # p1.start()

