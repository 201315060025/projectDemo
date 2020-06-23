# encoding: utf-8
"""
https://github.com/201315060025/test/blob/master/train/train.py
"""
from datetime import datetime
from path import Path

"""
todo: 1.  结合python的基本数据类型简述如何拷贝一个对象？
"""
def explain_copy():

    """
    拷贝对象
    浅拷贝： 没有拷贝子对象， 只拷贝最外层；
    eg: a = ["a", "v", {"name":"blx", "age":12}, "c"]
        b = copy.copy(a)
        当a中元素第三个元素变化， b 中的元素也会变化， 这个应该和python引用计数有关， 第三个元素的内存地址（id(obj)）是一样你的
    深拷贝： 包含对象中的子对象拷贝
    eg: a = ["a", "v", {"name":"blx", "age":12}, "c"]
        b = copy.deepcopy(a)
        当a中任意元素发生变化时， b中元素不会发生变化
    """
    pass


"""
todo: 2. 某人从1990年1月1日起开始“三天打鱼两天晒网”，问这个人在以后的某一天中是“打鱼”还是“晒网”。若输入时间小于开始时间或月份日期不合理，输出：“非法输入” 
"""

def fishing_basking(input_dt):
    """
    示例输入：1990-01-01 例输出：打鱼
    示例输入：1990-01-04 示例输出：晒网
    示例输入： 1990-01-32示例输出：非法输入
    """
    st_dt = "1990-01-01"
    if input_dt < st_dt:
        return "input datetime is invalid"
    try:
        cur_dt = datetime.strptime(input_dt, "%Y-%m-%d")
    except Exception as e:
        print("input datetime is invalid")
        return None
    total_day = (cur_dt - datetime.strptime(st_dt, "%Y-%m-%d")).days
    fishing_or_basking = total_day % 5
    if fishing_or_basking < 3:
        print("fishing")
    else:
        print("basking")


"""
todo: 3. 输入一个正整数N（N不大于100），输出一个n行的蛇形矩阵。
"""

def special_matrix(nums):
    """
    示例输入：
    5
    示例输出：
    1 3 6 10 15
    2 5 9 14
    4 8 13
    7 12
    11
    """

    first_num = 1
    for i in range(1, nums + 1):
        row_first = first_num
        if i == nums:
            print(row_first)
        else:
            print(row_first, end=" ")
        for j in range(i + 1, nums + 1):
            row_first += j
            if j == nums:
                print(row_first)
            else:
                print(row_first, end=" ")
        first_num += i

"""
todo: 4请结合restful原则设计一个URI：获取2019年12月，采购部的支出中大于10000元，小于50000元的数据列表，并按降序排列
"""
def Design_api():
    """
    eg: http://localhost?start_date="2019-01-01"&end_date="2019-01-01"& max_exp="10000"& min_max_exp="50000"*order=0
    因为接口设计参数灵活，
    例如时间， 如果单独传入年或则月， 获取的数据时间比较固定不宜扩展。
    """
    pass

"""
todo: 5数据库版本 oracle 11g，以下sql语句按顺序执行, 请问在非事务/事务两种方式下执行（执行前均认为tab_user已创建，无记录），name字段的值分别是什么，原因是什么。
insert into tab_user (name) values('abc') ;
update tab_user set name = 'efg';
select name from tab_user;
"""


def answer():
    """
    在非事务中输出结果是 efg; 在事务中输出结果null
    因为：oracle隔离级别是读已提交
    """

    pass


"""
todo: 6: windows平台下，目录 d:\dir 中有一百万个文件。使用walk和listbox遍历，内存消耗很大，运行速度也十分缓慢。请写出资源消耗小的遍历方法，并解释原因。
答案： 当文件夹下的文件过多时，可以考虑使用生成器， 遍历一个拿出一个， 减少内存的占用， 具体实现ergodic
"""

def ergodic(dir):
    # 列出所有文件和目录
    dir_list = Path(dir).glob("*")
    for dir_obj in dir_list:
        if dir_obj.isfile():
            print(str(dir_obj))
        else:
            ergodic(str(dir_obj))


def main():
    # test1
    explain_copy()
    # test2
    dt_list = ["1990-01-01", "1990-01-02", "1990-01-03", "1990-01-04", "1990-01-05", "1990-01-06", "1990-01-07",  "1989-01-01"]
    for dt in dt_list:
        fishing_basking(dt)

    # test3:
    for num in range(5, 20):
        special_matrix(num)

    # test4
    answer()
    # test5
    ergodic(".")

main()