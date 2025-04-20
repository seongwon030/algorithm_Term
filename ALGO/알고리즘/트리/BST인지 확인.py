import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize - 1

class Node:
    def  __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(node):
    return isBSTUtil(node, INT_MIN, INT_MAX)

def isBSTUtil(node, mini, maxi):
    if not node:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return isBSTUtil(node.left, mini, node.data - 1) and isBSTUtil(node.right, node.data + 1, maxi)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST(root)):
    print("Is BST")
else:
    print("Not a BST")