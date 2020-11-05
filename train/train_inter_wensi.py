# encoding: utf-8
"""
1.__init__()方法的作用是什么？
    初始化一个对象实列， 一般会定义该对象的属性； 而且是双下划线 也代表私有函数外界不能访问； 第一个参数必须是self

"""

"""
2: 单下划线、双下划线、头尾双下划线成员变量的区别是什么？
   头尾双下划线: 指定义的特殊方法，一般是系统定义比如__init__;  
   单下划线指受保护的变量，只能本省和子类可以调用，不能导入from ** import **
   双下划线：私有变量，只允许本身访问
"""

"""
3: self的作用是什么？
    实列对象本身，一般在类的方法中作为第一个参数参入；所有的方法和属性都绑定到self上
"""

"""
4: 类的多继承写法是什么
    如下
    Person 具有name, 和 sex属性； Woman 具有 say方法；
    而YoungGirl继承Person和 Woman
    
"""


class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


class Woman(object):

    def say(self):
        print("i am sing")
        pass


class YoungGirl(Person, Woman):
    pass


young_girl = YoungGirl(name="blx", sex="woman")
young_girl.say()

"""
5: 在python工程包的组织中，init.py的作用是什么
    把工程包当作一个python库，导入到其他文件; 一般和__all__ 使用控制模块的导入
"""

"""
6: 装饰器是什么？
    其实也是一个函数， 其作用在不改变原函数的基础上，为改函数增加额外的功能， 常见的有
    用户校验， log
"""

"""
7: numpy中如何获取一个numpy数组中最大值的索引值
"""
import numpy as np
arr = np.array([1, 2, 3, 4])
np.where(arr==max(arr))

"""
8: np.random.uniform函数作用是什么
随机采样； 参数有low, high, size;  注意low, high是左闭右开
"""

# 代码题

"""
1. 酷跑运动员爬梯子，每向上梯爬一节梯子需要6秒钟，而向下爬一层需要4秒钟，且每爬完1节，停留5秒钟。
假设运动员初始在地面，爬梯顺序如下：
输入：[1, 2]，输出：17
输入：[1,3,2,3,1]，输出：66
解答：
"""


def push_stairs(l_list):
    cast_time = 0
    num_1 = l_list[0]
    cast_time += 6
    for num in l_list[1:]:
        if num > num_1:
            cast_time += (num - num_1) * 6 + (num - num_1) * 5

        if num < num_1:
            cast_time += (num_1 - num) * 4 + (num_1 - num) * 5

        num_1 = num
    return cast_time


print("*"*10, "问答题1")
print("[1, 2]", push_stairs([1, 2]) == 17)
print("[1,3,2,3,1]", push_stairs([1,3,2,3,1]) == 66)

"""
2:打印如下数字三角形
n=5
1
2 12
3 13 11
4 14 15 10
5  6  7   8   9
解答：
"""


def rank_data(n):
    """
    生成一个三角形
    1            limit_value
    2 9          7
    3 10 8       5
    4 5  6 7     3
    :param n:
    :return:
    """
    if not n:
        return None

    # data = list(range(1, (1+n)/2))
    limit_value = {
        i: (n-1)-(i-n)*2 for i in list(range(1, n+1))[::-1] if i != 1
    }
    res = []
    for i in range(1, n+1):
        res.append([0]*i)

    for i in range(1, n+1):
        # i 是行数
        if i == n:
            # 最后一行规律比较明显
            res[i-1] = [i for i in range(i, i+limit_value[i]+1)]
        else:
            v = res[i-1]
            if 0 not in v:
                continue

            if len(v) == 1:
                res[i-1] = [i]
                continue
            if len(v) == 2:
                res[i-1] = [i, i+limit_value[i]]
                continue

            first_num = i
            last_num = i + limit_value[i]
            tmp_res = []
            for j in range(i):
                if j == 0:
                    # 如果是第一个元素
                    tmp_res.append(first_num)
                    pass
                elif j == i -1:
                    # 如果是最后一个元素
                    tmp_res.append(last_num)
                    pass
                elif j == 1:
                    tmp_res.append(res[i - 2][1]+1)
                else:
                    tmp_res.append(tmp_res[j-1]+1)
                    pass
            res[i-1] = tmp_res

    for dt in res:
        print(", ".join([str(ii) for ii in dt]))

rank_data(5)



"""
3.有如下字符串，包含3条关于水果数量的信息
“5 西瓜 苹果 蓝莓 苹果 苹果 3 桃 橙子 桃 0”
数字代表该数字后面出现的一组信息的水果数量，直到出现0为止，代表信息结束。
请输出每组信息中出现次数最多的水果。
（假设每组信息都保证有数量最多的1种水果）
解答：
"""

print("*"*10, "问答题3")


def count_fruits(fruits):
    fruit_list = fruits.split(" ")
    each_res = {}
    for cate in fruit_list:
        if cate.isdigit() and each_res:

            res = sorted(each_res.items(), key=lambda x:x[0], reverse=True)
            print(res[len(res)-1])
            each_res.clear()
        else:
            if cate.isdigit():continue
            if cate not in each_res:
                each_res[cate] = 0
            each_res[cate] +=1


tes = "5 西瓜 苹果 蓝莓 苹果 苹果 3 桃 橙子 桃 0"


count_fruits(tes)



