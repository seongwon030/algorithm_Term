import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 전위: root -> left -> right
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
        print(node.data, end='\n')


preorder = []
while True:
    try:
        n = int(input())
        if n == 0:
            break
        preorder.append(n)
    except:
        break

root = bst_from_preorder(preorder)
postorder(root)