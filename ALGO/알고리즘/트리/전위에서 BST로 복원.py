import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_from_preorder(preorder):
    def helper(lower, upper):
        nonlocal index
        if index == len(preorder):
            return None

        val = preorder[index]
        if val < lower or val > upper:
            return None

        index += 1
        node = Node(val)
        node.left = helper(lower, val - 1) # 왼쪽 서브트리는 현재값보다 작아야 하므로
        node.right = helper(val + 1, upper)
        return node

    index = 0
    return helper(-float('inf'), float('inf'))

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

preorder = [30, 20, 10, 15, 25, 23, 39, 35, 42]
root = bst_from_preorder(preorder)
postorder(root)