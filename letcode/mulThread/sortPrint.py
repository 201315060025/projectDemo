# encoding: utf-8
"""
不同的方法 按照有顺序的执行
url: https://leetcode-cn.com/problems/print-in-order/
我们提供了一个类：

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
三个不同的线程将会共用一个 Foo 实例。

线程 A 将会调用 first() 方法
线程 B 将会调用 second() 方法
线程 C 将会调用 third() 方法
请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。
"""
from threading import Thread,Lock, Semaphore, Condition
from time import sleep

def first(first_val):
    print(first_val)


def second(second_val):
    print(second_val)


def third(third_val):
    print(third_val)


class Foo(object):
    # 方法1：使用线程锁 先定义两个锁， 默认first先执行， second 执行只有first_lock释放， third执行 只有second_lock释放
    # 多线程下有顺序执行每个函数
    def __init__(self):
        self.first_lock = Lock()
        self.second_lock = Lock()
        # self.third_lock = Lock()
        # 获取锁
        self.first_lock.acquire()
        self.second_lock.acquire()

    def first(self, print_first_func: 'Callable[[], None]', first_val)->None:
        print_first_func(first_val)
        self.first_lock.release()

    def second(self, print_second_func: 'Callable[[], None]', second_val)-> None:
        with self.first_lock:
            print_second_func(second_val)
            self.second_lock.release()

    def third(self, print_third_func:"Callable[[], None]", third_val)->None:
        with self.second_lock:
            print_third_func(third_val)
            # self.third_lock.release()


def main1():
    foo = Foo()  # 执行
    callable_fun = [foo.first, foo.second, foo.third]
    callable_args = [first, second, third]
    val_list = ["first", "second", "third"]
    t1 = Thread(target=callable_fun[0], args=(callable_args[0], val_list[0], ))
    t2 = Thread(target=callable_fun[1], args=(callable_args[1], val_list[1], ))
    t3 = Thread(target=callable_fun[2], args=(callable_args[2], val_list[2], ))
    t3.start()
    t2.start()
    t1.start()


class Foo2(object):
    # 方法2：使用while循环 类似于信号量但是却不是信号量
    # 使用while 如果没有sleep while循环跑满CPU，会影响GIL线程上下文切换的判定，可能是导致超时的重要原因之一
    def __init__(self):
        self.single = 0

    def first(self, print_first_func: 'callable[[], None]', first_val)->None:
        print_first_func(first_val)
        self.single = 3

    def second(self, print_second_func: 'callable[[], None]', second_val)->None:
        while self.single != 2:
            sleep(1e-3)
        print_second_func(second_val)
        self.single = 3

    def third(self, print_second_func: 'callable[[], None]', third_val)->None:
        while self.single != 3:
            sleep(1e-3)
        print_second_func(third_val)


class Foo3(object):
    # 方法3 信号量机制
    def __init__(self):
        self.s1 = Semaphore(0)
        self.s2 = Semaphore(0)

    def first(self, print_first_func: 'callable[[], None]', first_val)->None:
        print_first_func(first_val)
        self.s1.release()

    def second(self, print_second_func: 'callable[[], None]', second_val)->None:
        self.s1.acquire()
        print_second_func(second_val)
        self.s2.release()

    def third(self, print_second_func: 'callable[[], None]', third_val)->None:
        self.s2.acquire()
        print_second_func(third_val)


class Foo4(object):
    # 启动wait_for来阻塞每个函数，直到指示self.t为目标值的时候才释放线程
    def __init__(self):
        self.c = Condition()
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.res(0, printFirst)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.res(1, printSecond)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.res(2, printThird)

    def res(self, val: int, func: 'Callable[[], None]') -> None:
        with self.c:
            self.c.wait_for(lambda: val == self.t)  # 参数是函数对象，返回值是bool类型
            func()
            self.t += 1
            self.c.notify_all()







