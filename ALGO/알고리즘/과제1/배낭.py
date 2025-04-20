N = int(input())
W = int(input())

items_weight = list(map(int, input().split()))
items_value = list(map(int, input().split()))

bag = []
for i in range(N):
    bag.append([items_weight[i], items_value[i]])

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        # j: 현재 배낭의 허용무게
        if j >= bag[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i-1][0]] + bag[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][W])