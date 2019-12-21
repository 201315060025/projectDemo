# encoding: utf-8
"""
二叉树方面的考点
"""


class Node:
    def __init__(self, data, left=None, right=None):
        """ 声明一个节点"""
        self.data = data
        self.left = left
        self.right = right

class B_Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, data):
        """add node"""
        node = Node(data)
        if self.root == None:
            self.root = node
            return

        queue = []
        queue.append(self.root)
        while True:
            curr_node = queue.pop(0)
            if curr_node.left == None:
                curr_node.left = node
                return
            elif curr_node.right == None:
                curr_node.right = node
                return

            else:
                queue.append(curr_node.left)
                queue.append(curr_node.right)

    def preorder(self, node):
        """
        先序遍历（前序遍历）：先访问根结点然后遍历左子树，最后遍历右子树
        从根节点开始，先遍历左子节点（到底）然后遍历右节点
        """
        if node == None:
            return
        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """

        :param node: root node
        :return:
        """
        if node == None:
            return

        self.inorder(node.right)
        print(node.data, end=' ')
        self.inorder(node.left)
        pass

    def postorder(self, node):
        """
        后序排序上同 中序排序
        :param node:
        :return:
        """
        if node == None:
            return
        self.postorder(node.left)
        print(node.data, end=" ")
        self.postorder(node.right)


if __name__ == '__main__':
    tree = B_Tree()
    for ii in range(6):
        tree.add(ii)

    print("inorder..")
    tree.inorder(tree.root)
    print('\n' * 2)
    print("preorder..")
    tree.preorder(tree.root)
    print("\n"*2)
    print("postorder..")
    tree.postorder(tree.root)