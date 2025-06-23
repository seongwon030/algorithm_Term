def bst_post_to_pre(left, right):
    if left > right:
        return

    # 루트 노드 찾기
    root = post_list[right]
    idx = None

    for i in range(right-1, left - 1, -1):
        if post_list[i] < root:
            idx = i
            break

    # 왼쪽 서브트리가 없는 경우 (= 루트보다 작은 값이 하나도 없다면)
    if idx is None:
        idx = left - 1

    print(root, end=' ')
    bst_post_to_pre(left, idx)
    bst_post_to_pre(idx+1, right-1)

n = int(input())
post_list = list(map(int, input().split()))
bst_post_to_pre(0, len(post_list) - 1)