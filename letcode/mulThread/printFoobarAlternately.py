# encoding: utf-8
"""
不同的方法 按照有顺序的执行  --> 循环
url: https://leetcode-cn.com/problems/print-foobar-alternately/
我们提供一个类：

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。

请设计修改程序，以确保 "foobar" 被输出 n 次。
"""
from threading import Thread, Semaphore
import time


def print_foo():
    print("foo", end=" ")


def print_bar():
    print("bar", end=" ")


def print_hello():
    print("hello", end=" ")


def print_world():
    print("world", end=" ")


class FooBar(object):
    def __init__(self, num):
        self.num = num
        self.s1 = Semaphore(0)
        self.s2 = Semaphore(1)
        self.s3 = Semaphore(2)
        self.s4 = Semaphore(3)

    def foo(self, printFoo: 'callable[[], None]')->None:
        for i in range(self.num):
            self.s1.acquire()
            printFoo()
            self.s2.release()

    def bar(self, printBar: 'callable[[], None]')->None:
        for i in range(self.num):
            self.s2.acquire()
            printBar()
            self.s1.release()
    # def hello(self, printHello: 'callable([], None)')->:
    #     for i in range(self.num):
    #         self.s3.acquire()
    #         printHello()
    #         self.s3.release()


def test_main():
    foo_bar = FooBar(4)
    callable_fun = [foo_bar.foo, foo_bar.bar]
    callable_args = [print_foo, print_bar]

    t1 = Thread(target=callable_fun[1], args=(callable_args[1],))
    t2 = Thread(target=callable_fun[0], args=(callable_args[0], ))

    t1.start()
    t2.start()


test_main()