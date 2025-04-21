class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

if __name__ == '__main__':
    n = int(input())
    nodes = {i: Node(i) for i in range(n)}
    root = None

    print(nodes)

    for child in range(n):
        parent_str, dir = input().split()

        if  parent_str == '-1': # -1인 경우 루트노드
            root = nodes[child]
        else:
            parent = int(parent_str)

            if dir == 'L':
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)