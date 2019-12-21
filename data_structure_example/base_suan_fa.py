# coding: utf-8

def bud_rank():
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
    a = [2, 4, 1, 6, 3, 5]
    ln = len(a)
    for i in range(1, ln):
        for j in range(1, i):
            if a[i - 1] > a[j]:
                tmp = a[j - 1]
                a[i - 1] = a[j]
                a[j] = tmp
    print("insert rank result")
    print(a)
    print("\n" * 2)


def quily_rank():
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
    """希尔排序"""
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
