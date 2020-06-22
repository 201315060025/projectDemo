# encoding: utf-8
"""
队列操作
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""

class Queue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        """添加元素"""
        self.queue.append(item)

    def dequeue(self, item):
        """从头部删除一个元素"""
        self.queue.pop(0)

