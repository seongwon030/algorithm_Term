class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node:
        print(node.data, end=' ')

        inorder(node.left)

        print(node.data, end=' ')

        inorder(node.right)


if __name__ == '__main__':
    n = int(input())

    nodes = {}
    for _ in range(n):
        parent, left, right = map(int, input().split())
        if parent not in nodes:
            nodes[parent] = Node(parent)
        if left != -1 and left not in nodes:
            nodes[left] = Node(left)
        if right != -1 and right not in nodes:
            nodes[right] = Node(right)

        nodes[parent].left = nodes[left] if left != -1 else None
        nodes[parent].right = nodes[right] if right != -1 else None

    visit_count = [0] * (n + 1)
    root = nodes[1]

    inorder(root)