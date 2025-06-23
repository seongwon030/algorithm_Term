class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst_postorder(postorder):
    def check_bst(postorder, start, end):
        if start > end:
            return 0

        root = postorder[end]
        split = start
        while split < end and postorder[split] < root:
            split += 1

        for i in range(split, end):
            if postorder[i] < root:
                return -1

        left_height = check_bst(postorder, start, split - 1)
        right_height = check_bst(postorder, split, end - 1)

        if left_height == -1 or right_height == -1:
            return -1

        return max(left_height, right_height) + 1

    height = check_bst(postorder, 0, len(postorder) - 1)
    return height if height >= 0 else -1


n = int(input())
postorder = list(map(int, input().split()))

height = is_bst_postorder(postorder)
print(height)
