class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(inorder, postorder, in_s, in_e):
    global p_idx
    if in_s > in_e:
        return None

    # postorder에서 현재 루트 노드 가져오기
    if p_idx < 0:
        return None  # postorder 다 소비한 경우

    node = Node(postorder[p_idx])
    p_idx -= 1

    index = search(inorder, in_s, in_e, node.value)
    if index == -1:
        global build_failed
        build_failed = True
        return None

    node.right = build_tree(inorder, postorder, index + 1, in_e)
    node.left = build_tree(inorder, postorder, in_s, index - 1)

    return node

def search(inorder, start, end, target):
    for i in range(start, end + 1):
        if inorder[i] == target:
            return i
    return -1

def preorder_traversal(node):
    if node:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def main():
    global p_idx, build_failed
    postorder = [10, 9, 23, 22, 27, 25, 15, 50, 95, 60, 40, 29]
    # postorder = list(map(int, input("Postorder 입력: ").replace(' ', '').split(',')))
    inorder = list(map(int, input("Inorder 입력: ").replace(' ', '').split(',')))

    p_idx = len(postorder) - 1
    build_failed = False

    root = build_tree(inorder, postorder, 0, len(inorder) - 1)

    if build_failed or root is None:
        print("🚫 잘못된 inorder / postorder 조합입니다.")
    else:
        print("✅ Preorder:")
        preorder_traversal(root)

main()
