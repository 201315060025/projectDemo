# encoding: utf-8
"""
单链表
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

class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next

        return count


    def tracel(self):
        """遍历"""
        cur = self._head
        while cur.next != None:
            print(cur.item)
            cur = cur.next
        pass

    def add(self, item):
        """头部添加"""
        node  = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """尾部添加"""
        node = SingleNode(item)
        # 判断是否为空，
        if self.is_empty():
            self._head = node
            return None

        current_node = self._head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = node

    def insert(self, pos, item):
        """
        指定位置添加
        1： 验证是否是头部
        2： 验证是否是尾部
        """
        if pos<= 0:
            self.add(item)

        elif pos > self.length():
            self.append(item)
        else:
            node = SingleNode(item)
            pre = self._head
            count = 0
            # 此处不是循环链表， 如果插入索引的长度 大于 链表长度  没有条件pre ！= None 应该会报错。。。
            while pre != None or count != pos:
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def remove(self, item):
        pass

    def search(self, item):
        """
        检查节点是否存在
        """
        current_node = self._head
        flag = True
        while current_node.item != item:
            if current_node.next == None:
                flag = False
                # break
            current_node = current_node.next
        return flag

    def hasCycle(self):
        """
        判断是否有环
        判断一个单链表是否有环,
        可以用 set 存放每一个 节点, 这样每次 访问后把节点丢到这个集合里面.
        其实 可以遍历这个单链表, 访问过后,
        如果这个节点 不在 set  里面, 把这个节点放入到 set 集合里面.
        如果这个节点在  set 里面 , 说明曾经访问过, 所以这个链表有重新 走到了这个节点, 因此一定有环.

        如果链表都走完了, 把所有的节点都放完了. 还是没有重复的节点, 那说明没有环.
        """
        nums = set()
        current_node = self._head
        flag = True
        while current_node.next != None:
            if current_node.item not in nums:
                nums.add(current_node.item)
            else:
                flag = False
        return flag


if __name__ == "__main__":
    single_link_list = SingleLinkList()
    single_link_list.add(2)
    single_link_list.add(4)
    single_link_list.add(3)
    print(f"single link list length = {single_link_list.length()}")
    print(f"single link list null = {single_link_list.is_empty()}")
    # 遍历
    single_link_list.tracel()
    #
    pass