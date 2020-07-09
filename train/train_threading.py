# encoding: utf-8
"""
线程操作
start() 线程就绪 准备cpu调用
setName()  设置线程名称
getName() 获取线程名称
setDaemon
join() 逐步执行每个线程
run() 线程被

exam1：
    声明线程； 执行start(); 最后执行join()
exam2:
    使用继承方式threading.Thread
exam3:
    线程中嵌套线程 主线程和子线程 daemon

"""
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed


def train1():
    """
    普遍的线程写法
    :return:
    """
    def thread_fun(name, tt):
        print("hello, {0}".format(name))
        time.sleep(tt)
        print("{0} exe end.".format(name))

    t1 = threading.Thread(target=thread_fun, args=("blx1",3,))
    t2 = threading.Thread(target=thread_fun, args=("blx2", 1,))
    t1.setName("thread1")
    t2.setName("thread2")
    t1.start()
    t2.start()

class Train2(threading.Thread):
    def __init__(self, name, tt):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep_time = tt

    def run(self):
        print("{0} hello, {1}".format(time.ctime(), self.name))
        time.sleep(self.sleep_time)
        print("{0}-(1), exe end.".format(time.ctime(), self.name))

def train2():
    """
    继承线程类的写法
    :return:
    """
    t1 = Train2("thread1", 3)
    t2 = Train2("thread2", 1)
    t1.start()
    t2.start()

def train3():
    """
    父子线程
    :return:
    """
    def thread_fun(name, tt):
        print("hello, {0}".format(name))
        time.sleep(tt)
        print("{0} exe end.".format(name))

    def main():

        t1 = threading.Thread(target=thread_fun, args=("blx1",3,))
        t2 = threading.Thread(target=thread_fun, args=("blx2", 1,))
        t1.setName("thread1")
        t2.setName("thread2")
        t1.start()
        t2.start()
        t1.join(1)
        t2.join(1)

    p_t = threading.Thread(target=main, args=())
    # 一般置为False
    # 将主线程设置Daemon设置为True后,主线程执行完成时,其它子线程会同时退出,不管是否执行完任务
    p_t.setDaemon(False)
    p_t.start()
    p_t.join()
    print("end..")

num = 100
lock=threading.Lock()
def train4():
    """
    线程锁的考点
    :return:
    """

    def tread_func(name, tt):
        global num
        global lock
        lock.acquire()
        print("hello, {0}".format(name))
        time.sleep(tt)
        num -= 1
        print("{0}, num={1}".format(name, str(num)))
        print("{0} end.".format(name))
        lock.release()

    thread_list = []
    for i in range(1,100):
        t = threading.Thread(target=tread_func, args=("thread"+str(i), 1, ))
        t.start()
        thread_list.append(t)

    for thread_obj in thread_list:
        thread_obj.join()

def train5():
    """
    使用线程池 声明多线程

    sumbit()  执行函数
    done  判断线程是否执行完成
    result 获取执行结果
    :return:
    """
    def thread_fun(name, tt=1):
        print("{0}: hello, {1}".format(str(time.time()), name))
        time.sleep(tt)
        print("{0}: {1} exe end.".format(str(time.time()), name))

    with ThreadPoolExecutor(max_workers=5) as t:
        task1 = t.submit(thread_fun, "thread1", 1)
        task2 = t.submit(thread_fun, "thread2", 2)
        task3 = t.submit(thread_fun, "thread3", 3)

        print("task1: ", task1.done())
        print("task2: ", task2.done())
        print("task3: ", task3.done())
    time.sleep(3)
    print("task1: ", task1.done())
    print("task2: ", task2.done())
    print("task3: ", task3.done())
    pass

def train6():
    """
    线程池 as_completed
    :return:
    """
    def thread_fun(name, tt=1):
        print("{0}: hello, {1}".format(str(time.time()), name))
        time.sleep(tt)
        print("{0}: {1} exe end.".format(str(time.time()), name))
        return name

    with ThreadPoolExecutor(max_workers=5) as t:
        tt_list = [t.submit(thread_fun,"thread"+str(i), i)  for i in range(1,4)]
        for tt in as_completed(tt_list):
            data = tt.result()
            print("thread==", data)


    pass


if __name__ == "__main__":
    print("简单线程写法")
    # train1()
    print("继承类的写法")
    # train2()
    print("父子线程")
    # train3()
    print("线程测试 不加锁")
    # train4()
    print("线程池测试 sumbit")
    # train5()
    print("线程池测试 as_completed")
    train6()
