from collections import deque

class Node:
    def  __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 중위순회 : 루트 -> 왼쪽 -> 오른쪽
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

# 전위순회 : 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

# 후위순회 : 왼쪽 -> 오른쪽 -> 루트
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

def level_order(node):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def build_tree():
    fox = Node("fox")
    bear = Node("bear")
    goose = Node("goose")
    ant = Node("ant")
    dog = Node("dog")
    hippo = Node("hippo")
    cat = Node("cat")
    eagle = Node("eagle")
    iguana = Node("iguana")

    fox.left = bear
    fox.right = goose

    bear.left = ant
    bear.right = dog

    dog.left = cat
    dog.right = eagle

    goose.right = hippo
    hippo.right = iguana

    return fox

if __name__ == "__main__":
    root = build_tree()

    print("Inorder:")
    inorder(root)
    print("\nPreorder:")
    preorder(root)
    print("\nPostorder:")
    postorder(root)
    print("\nLevel Order:")
    level_order(root)