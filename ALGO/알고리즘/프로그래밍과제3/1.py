class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')


if __name__ == '__main__':
    nodes = {}

    with open('input1.txt', 'r') as f:
        lines = f.read().strip().splitlines()

    n = int(lines[0])
    for i in range(1, n+1):
        parent, left, right = lines[i].split()
        if parent not in nodes:
            nodes[parent] = Node(parent)

        if left != '-1':
            if left not in nodes:
                nodes[left] = Node(left)
            nodes[parent].left = nodes[left]
        else:
            nodes[parent].left = None

        if right != '-1':
            if right not in nodes:
                nodes[right] = Node(right)
            nodes[parent].right = nodes[right]
        else:
            nodes[parent].right = None


    child_nodes = set()
    for node in nodes.values():
        if node.left:
            child_nodes.add(node.left.data)
        if node.right:
            child_nodes.add(node.right.data)

    root = None
    for node in nodes.values():
        if node.data not in child_nodes:
            root = node
            break

    preorder(nodes[root.data])
    print()
    inorder(nodes[root.data])
    print()
    postorder(nodes[root.data])
