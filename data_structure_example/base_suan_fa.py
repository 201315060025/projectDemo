# coding: utf-8

def bud_rank():
    """
    冒泡排序：两两排序 相邻的两个元素交换位置
    时间复杂度 最优O（n） 最差是O(n**2)
    稳定
    """
    a = [2, 4, 1, 6, 3, 5]
    ln = len(a)
    for i in range(ln):
        for j in range(1, ln):
            if a[j-1] > a[j]:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp

    print("bud_rank result")
    print(a)
    print("\n"*2)


def insert_rank():
    """
    插入排序：对未排序的数据，在已排序的数据中从后向前扫描，找到相应的位置插入
    时间复杂度 最优O（n） 最差是O(n**2)
    稳定
    """
    a = [2, 4, 1, 6, 3, 5]
    ln = len(a)
    for i in range(1, ln):
        for j in range(1, i):
            if a[i-1] > a[j]:
                tmp = a[j - 1]
                a[j - 1] = a[j]
                a[j] = tmp
    print("insert rank result")
    print(a)
    print("\n"*2)

def select_rank():
    """
    选择排序： 在未排序的序列中找出最大（小）值，放到排序序列的起始位置。
    时间复杂度 最优O(n**2) 最差是O(n**2)
    不稳定
    """
    a = [2, 4, 1, 6, 3, 5]
    ln = len(a)
    for i in range(ln-1):
        # 声明最小值的索引
        min_idx = i
        for j in range(i+1, ln):
            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            a[i], a[min_idx] = a[i], a[min_idx]

    print("select rank result")
    print(a)
    print("\n" * 2)


def quily_rank():
    """
    快速排序： 划分交换排序，通过第一堂数据将要排序的数据分割成独立的两部分。

    """
    a = [2, 4, 1, 6, 3, 5]

    def quily_rank_obj(items):
        if len(items) <= 1:
            return items
        else:
            base = items[0]
            left = [num for num in items if num < base]
            right = [num for num in items if num > base]
            return quily_rank_obj(left) + [base] + quily_rank_obj(right)

    b = quily_rank_obj(a)
    print(b)
    print("\n"*2)


def shell_rank():
    """
    希尔排序: 步长排序， 将数字列在一个表中， 并对每个列进行插入排序， 重复这个过程， 不过每次使用的步长列
    最优时间复杂度：根据步长序列的不同而不同
    最坏：O(n**2)
    不稳定
    """
    items = [2, 4, 1, 6, 3, 5]
    ln = len(items)
    sep = ln // 2
    while sep > 0:
        for i in range(sep, ln):

            while i >= sep and items[i-sep] > items[i]:
                items[i-sep], items[i] = items[i], items[i-sep]
                i -= sep
        sep = sep // 2

    print("shell rank result")
    print(items)
    print("\n"*2)


def meger_rank():
    """归并排序"""
    pass


def iteration():
    """输出1*2*3*4*5"""

    def iter_mul(num):
        if num <1:
            return num
        else:
            return num * iter_mul(num-1)


if __name__ == "__main__":
    bud_rank()
    insert_rank()
    quily_rank()
    shell_rank()
