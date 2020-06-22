# encoding: utf-8
"""
单向循环链表
单链表的一个变形是单向循环链表，链表中最后一个节点的next域不再为None，而是指向链表的头节点
链表的基本操作：
1: is_empty
2: length
3: travel 遍历
4: 头部添加  add
5: 尾部添加 append()
6: 任意位置插入： insert()
7: 删除节点 ： remove
8: 查找节点 seache
"""


class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCycLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        """计算长度"""
        if self.is_empty():
            return 0
        count = 1
        current_node = self._head
        while current_node.next != self._head:
            count += 1
            current_node = current_node.next

        return count

    def travel(self):
        """遍历"""
        if self.is_empty():
            print("not..")
        else:
            current_node = self._head
            print(f"current value {str(current_node.item)}")
            while current_node.next != self._head:
                print(f"current value {str(current_node.next.item)}")
                current_node = current_node.next

    def add(self, item):
        """"""
        new_node = SingleNode(item)
        if self.is_empty():
            self._head = new_node
            new_node.next = self._head
        else:
            # new_node.next = self._head
            current_node = self._head
            while current_node.next != self._head:
                current_node = current_node.next

            new_node.next = self._head
            current_node.next = new_node
            # ??
            self._head = new_node

    def append(self, item):
        new_node = SingleNode(item)
        if self.is_empty():
            self._head = new_node
            new_node.next = self._head
        else:
            current_node = self._head
            while current_node.next != self._head:
                current_node = current_node.next

            current_node.next = new_node
            new_node.next = self._head

    def insert(self, pros, item):
        new_node = SingleNode(item)
        if self.is_empty():
            self._head = new_node
            new_node.next = self._head
        else:
            current_node = self._head
            next_node = current_node.next
            count = 0
            while count < (pros-1):
                current_node = next_node
                next_node = current_node.next
                count += 1

            current_node.next = new_node
            new_node.next = next_node

    def remove(self, item):
        pass

    def search(self, item):
        pass


if __name__ == "__main__":
    ll = SingleCycLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(7))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()




