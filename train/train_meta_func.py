# encoding: utf-8
"""
https://www.cnblogs.com/shenxiaolin/p/9307496.html
python 中的__new__ __init__ __str__
他们之间的先后顺序
首先调用的是__new__ 其次是__init__ 最后是__str__
__new__的官方文档解释是：继承一些不可改变的class时
自定义metaclass
"""

class Person(object):
    """
    str函数或者print函数调用时 = obj.__srt__()
　　repr函数或者交互式解释器中调用时 = obj.__repr__()
    """
    def __new__(cls, name, age):
        print("in __new__ called")
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print("init __init__ called")
        self.name = name
        self.age = age

    def __str__(self):
        """对象的描述"""
        print("in __str__ called")
        return "<person:%s(%s)>"%(self.name, self.age)

    def __repr__(self):
        return 'repr:我叫{}，今年{}岁'.format(self.name, self.age)


class SiglePerson:
    __instance=None
    __init_flag = False
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if SiglePerson.__init_flag == False:
            self.name = "blx"
            self.age = 22
            SiglePerson.__init_flag = True


class test1():
    """
    可迭代对象
    test ：
    for i in test1():
        print(i)
    for .. in .. 其实做了两件事
    1： __iter__ 获取可迭代对象
    2: 循环调用 __next__
    因为该类具有__iter__和__next__ 函数 所以它是可迭代的对象
    """
    def __init__(self,data=1):
        self.data = data

    def __iter__(self):
        return self
    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data+=1
            return self.data

class test2():
    """
    迭代器
    test
    tt = test(3)
    for i in range(3):
        print(t.__next__())
    含有__next__函数所以tt实一个迭代器
    """
    def __init__(self,data=1):
        self.data = data

    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data+=1
            return self.data


def fib(end = 1000):
    """
    生成器
    test
    print(list(fib()))

    其实生成器是一种特殊的迭代器， 因为它具有__next__方法
    其返回值不用return 而用yied
    :param end:
    :return:
    """
    prev,curr=0,1
    while curr < end:
        yield curr
        prev,curr=curr,curr+prev


class TmpTest:
    """
    上下文管理器
    test
    test = TmpTest("test.txt")
    with test as t:
        print("")

    实现了__enter__() __exist__() 两个方法的对象， 就叫做上下文管理器
    其中__enter__() 在使用with语句调用， 会话管理器执行代码前调用， 返回值与as 结合
    __exit()__  会话管理器执行完代码with 语句结束后， 对象销毁
    """
    def __init__(self,filename):
        self.filename=filename
        print("__init__")
        # raise ImportError
    def __enter__(self):
        self.f = open(self.filename, 'r')
        print("__enter__")
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.f.close()

class Test3(object):
    """
    可调用对象； 我们平时定义的函数，方法， 类都属于可调用对象； 但凡能拿都一对括号（）使用在身上的都是可调用对象；
    如果实现了__call__（）方法就是可调用对象
    """
    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
            '''改变实体的位置'''
            self.x, self.y = x, y

class CLanguage:
    """
    test:
    clangs = CLanguage()
    if hasattr(clangs,"name"):
        print(hasattr(clangs.name,"__call__"))
    print("**********")
    if hasattr(clangs,"say"):
        print(hasattr(clangs.say,"__call__"))
    弥补hasttr 的缺点
    hasttr 第二个参数可能是“属性”， 也可能是“方法”
	所以当传入参数时， 返回值是True,
    但是不能判断该参数是 “属性”还是“方法”
    """
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say(self):
        print("我正在学Python")

class Person2:
    """
    对象字段化操作
    __getItem__, __setItem__, __deleteItem__
    """
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def __getitem__(self, item):
        if hasattr(self, item):
            return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

if __name__ == "__main__":
    pe = Person("blx",  "22")
    print(pe)
    print("测试单列模式")
    # 测试单列模式
    p1 = SiglePerson()
    print("name=%s, age=%s"%(p1.name, str(p1.name)))
    p1.name = "test"
    print("name=%s, age=%s"%(p1.name, str(p1.name)))
    p2 = SiglePerson()
    print(p1==p2)
    print("name=%s, age=%s"%(p2.name, str(p2.name)))
    print("\n"*2)
    # 可迭代对象
    print("可迭代对象")
    for i in test1():
        print(i)
    # 迭代器
    print("迭代器")
    tt = test2(3)
    for i in range(3):
        print(tt.__next__())
    # 生成器
    print("生成器")

    print("\n"*2)
    print("上下文管理器")
    test = TmpTest("E://interviewTest//test//train//train.py")
    with test as t:
        print(t)

    print("\n"*2)
    print("可调用对象")
    test_obj = Test3(3,4,5)
    print("x={0}, y={1}".format(str(test_obj.x), str(test_obj.y)))
    print("------------")
    test_obj(33,44)
    print("x={0}, y={1}".format(str(test_obj.x), str(test_obj.y)))

    print("\n"*2)
    print("对象属性字典化")
    p = Person2("blx", "22", "pingpang")
    print(p.name) # 通过原始方法获取
    print(p["name"])  # 通过字典获取
    p["name"] = "blx123"
    print(p.__dict__)
    del p["name"]
    print(p.__dict__)





