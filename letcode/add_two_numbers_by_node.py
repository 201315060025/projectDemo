# encoding:utf-8
"""
https://leetcode-cn.com/problems/add-two-numbers/solution/76ms137mb-by-yue-xia-gua-tian-de-run-tu/
todo: 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None



class Solution(object):
    def add_two_nums(self, nums1: ListNode, nums2: ListNode)-> list:
        res = []
        digit = 0
        while nums1 or nums2:
            num_obj_1 = nums1 if nums1 else 0
            num_obj_2 = nums2 if nums2 else 0
            sum_obj = num_obj_1.data + num_obj_2.data
            if digit > 0:
                    sum_obj += digit
                    digit = 0
            if sum_obj >= 10:
                digit = 1
                sum_obj -= 10

            res.append(sum_obj)
            nums1 = nums1.next
            nums2 = nums2.next
        return res


if __name__ == "__main__":
    # 声明 链表1
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    list_node_1 = node1

    # 声明 链表2
    node21 = ListNode(5)
    node22 = ListNode(6)
    node23 = ListNode(4)
    node21.next = node22
    node22.next = node23
    list_node_2 = node21
    # exe
    print(Solution().add_two_nums(list_node_1, list_node_2))

