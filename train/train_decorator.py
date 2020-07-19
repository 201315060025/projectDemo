# encoding: utf-8
"""
装饰器： 在不改变原函数的情况下， 为函数增加行的功能， 例如 日志
"""

# 简单的案例
"""
记住-->两个装饰器的执行顺序
"""
import time

def decorator_f1_1(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

def decorator_f1_2(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped

@decorator_f1_2
@decorator_f1_1
def f1():
    return "hello world"

print(f1())



"""
为函数添加额外的功能
假设有一个函数，， 添加装饰器 计算该函数的运行时间
"""
print("\n"*2)
print("-"*10)
def decorator_f2_1(func):
    def wrapped():
        t1 = time.time()
        print("start time: ", t1)
        func()
        t2 = time.time()
        print("end time: ", t2)
        print("hao shi:", t2 - t1)
        return func()
    return wrapped


@decorator_f2_1
def f2():
    print("start.")
    time.sleep(2)
    print("end..")


f2()



