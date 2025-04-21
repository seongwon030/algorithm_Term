class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(inorder, postorder):
    inorder_index_map = {val: i for i, val in enumerate(inorder)}
    post_idx = [len(postorder) - 1]  # 후위 인덱스를 리스트로 (mutable)

    def helper(in_left, in_right):
        if in_left > in_right:
            return None

        root_val = postorder[post_idx[0]]
        root = Node(root_val)
        post_idx[0] -= 1

        # 중위순회에서 루트위치
        in_root_idx = inorder_index_map[root_val]

        # 루트를 맨 끝에서부터 꺼내므로 재귀는 오른쪽부터 구성
        root.right = helper(in_root_idx + 1, in_right)
        root.left = helper(in_left, in_root_idx - 1)

        return root

    return helper(0, len(inorder) - 1)
