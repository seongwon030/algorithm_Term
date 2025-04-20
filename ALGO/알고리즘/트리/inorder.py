class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

if __name__ == '__main__':
    root = None
    nodes = list(map(int, input().replace(' ', '').split(',')))

    for n in nodes:
        root = insert(root, n)

    inorder(root)