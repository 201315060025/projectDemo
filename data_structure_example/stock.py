# encoding: utf-8
"""
栈操作
栈可以用列表实现也可以用链表实现
以下是用列表实现
栈的主要操作
1：查看栈是否为空
2：查看栈的大小
3: 添加元素
3：弹出栈顶元素
4：返回栈顶元素
"""

class Stock():
    def __init(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def peek(self):
        return self.items[self.size()]

    def pop(self):
        return self.items.pop()

