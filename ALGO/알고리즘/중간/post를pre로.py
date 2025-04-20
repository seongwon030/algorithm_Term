import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_from_postorder(postorder):
    def helper(lower, upper):
        nonlocal index
        if index < 0:
            return None

        val = postorder[index]
        if val < lower or val > upper:
            return None

        index -= 1
        node = Node(val)
        node.right = helper(val + 1, upper)
        node.left = helper(lower, val - 1) # 왼쪽 서브트리는 현재값보다 작아야 하므로
        return node

    index = len(postorder) - 1
    return helper(-float('inf'), float('inf'))

def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

n = int(input())
postorder = list(map(int, input().split()))
root = bst_from_postorder(postorder)
preorder(root)