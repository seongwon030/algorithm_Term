def max_stackable_boxes(weights, capacities):
    n = len(weights)
    INF = float('inf')

    # T[i][k]: i번째 상자부터 N까지 중에서 k개를 선택했을 때 최소 위 하중
    T = [[INF] * (n+1) for _ in range(n+2)]

    # k = 0일 때는 항상 무게합 0으로 가능
    for i in range(n+2):
        T[i][0] = 0

    for i in range(n, 0, -1):
        # 현재 상자의 무게, 현재 상자의 허용 하중
        w,c = weights[i-1], capacities[i-1]
        for k in range(1, n+1):
            # 쌓는 상자 개수 1부터 N까지 반복
            if T[i+1][k-1] <= c:
                # 현재 상자 i를 아래에 두고 K번째로 쌓기 가능
                T[i][k] = min(T[i + 1][k], T[i + 1][k - 1] + w)
            else:
                T[i][k] = T[i + 1][k]

    for k in range(n, -1, -1):
        if T[1][k] != INF:
            return k

    return 0

weights = [5, 3, 2]
capacities = [10, 7, 9]
print(max_stackable_boxes(weights, capacities))  # 출력: 3