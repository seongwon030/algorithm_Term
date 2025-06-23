n = int(input())
W = int(input())

dp = [[0] * (W+1) for _ in range(n+1)]

w_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

bag = []
for i in range(n):
    bag.append([w_list[i], v_list[i]])

for i in range(1, n+1):
    for j in range(1, W+1):
        if j >= bag[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i-1][0]] + bag[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][W])