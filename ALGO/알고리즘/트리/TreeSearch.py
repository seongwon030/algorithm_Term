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

# 재귀 탐색
# 스택을 이용해 다음 위치로 점프
def tree_search(node, target):
    if not node or node.data == target:
        return node
    if target < node.data:
        return tree_search(node.left, target)
    else:
        return tree_search(node.right, target)

# 반복탐색
# 직접 포인터를 옮기면서 순회
def interactive_tree_search(node, target):
    while node is not None and target is not node.data:
        if target < node.data:
            node = node.left
        else:
            node = node.right
    return node

def tree_min(node):
    while node.left is not None:
        node = node.left
    return node

def tree_max(node):
    while node.right is not None:
        node = node.right
    return node

def find_successor(node, root):
    if node.right is not None:
        return tree_min(node.right)

    successor = None
    current = root
    while current is not None:
        if node.data < current.data:
            successor = current
            current = current.left
        elif node.data > current.data:
            current = current.right
        else:
            break
    return successor

def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None and root.right is None:
            return None
        # 1. 자식 노드가 없는 경우 바로 삭제
        if root.left is None and root.right is None:
            return None
        # 2. 자식 노드가 1개인 경우 자신의 자식 노드를 원래 자신의 위치로
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # 3. 자식 노드가 2개인 경우 삭제 하려는 노드의 successor copy 후 삭제
        successor = tree_min(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root


if __name__ == '__main__':
    root = None
    nodes = [15,6,18,3,7,17, 20,2,4,13,9]

    for n in nodes:
        root = insert(root, n)

    result = tree_search(root, 13)
    if result:
        print(f"찾음: {result.data}")
    else:
        print("못 찾음")

    result2 = interactive_tree_search(root, 13)
    if result2:
        print(f"찾음: {result2.data}")
    else:
        print("못 찾음")

    min_node = tree_min(root)
    print(min_node.data)

    max_node = tree_max(root)
    print(max_node.data)

    target = tree_search(root, 13)
    succ = find_successor(target, root)
    print(succ.data)

    # 삭제
    root = delete(root, 13)  # 반드시 root = delete(...)로 갱신해줘야 함

    # 삭제 후 탐색 결과
    result = tree_search(root, 13)
    if result:
        print("삭제 실패, 여전히 있음:", result.data)
    else:
        print("13 삭제 완료")