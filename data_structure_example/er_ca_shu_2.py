import math

class BTNode(object):
    """docstring for BTNode"""
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# insert element
def InsertElementBinaryTree(root, node):
    if root:
        if node.data < root.data:
            if root.leftChild:
                InsertElementBinaryTree(root.leftChild, node)
            else:
                root.leftChild = node
        else:
            if root.rightChild:
                InsertElementBinaryTree(root.rightChild, node)
            else:
                root.rightChild = node
    else:
        return 0

# init a tree
def InitBinaryTree(dataSource, length):
    root = BTNode(dataSource[0])

    for x in range(1,length):
        node = BTNode(dataSource[x])
        InsertElementBinaryTree(root, node)
    return root


# pre-order
def PreorderTraversalBinaryTree(root):
    if root:
        print('%d | ' % root.data)
        PreorderTraversalBinaryTree(root.leftChild)
        PreorderTraversalBinaryTree(root.rightChild)

# in-order
def InorderTraversalBinaryTree(root):
    if root:
        InorderTraversalBinaryTree(root.leftChild)
        print('%d | ' % root.data)
        InorderTraversalBinaryTree(root.rightChild)

# post-order
def PostorderTraversalBinaryTree(root):
    if root:
        PostorderTraversalBinaryTree(root.leftChild)
        PostorderTraversalBinaryTree(root.rightChild)
        print('%d | ' % root.data)

# layer-order
def TraversalByLayer(root, length):
    stack = []
    stack.append(root)
    for x in range(length):
        node = stack[x]
        print('%d | ' % node.data)
        if node.leftChild:
            stack.append(node.leftChild)
        if node.rightChild:
            stack.append(node.rightChild)


if __name__ == '__main__':
    dataSource = [0,1,2,3,4,5]
    length = len(dataSource)
    BTree = InitBinaryTree(dataSource, length)
    print('****NLR:')
    PreorderTraversalBinaryTree(BTree)
    print( '\n****LNR')
    InorderTraversalBinaryTree(BTree)
    print('\n****LRN')
    PostorderTraversalBinaryTree(BTree)
