def min_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    dp[0][0] = grid[0][0]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[n-1][n-1]

grid = [
    [6, 7, 12, 5],
    [5, 3, 11, 18],
    [7, 17, 3, 3],
    [8, 10, 14, 9]
]

print(min_path_sum(grid))