MAX = 100
binom = [[-1 for _ in range(MAX)] for _ in range(MAX)]

# 1. 메모이제이션 + 재귀 방식 (Top-down)
def binomial(n, k):
    if n == k or k == 0:
        return 1
    elif binom[n][k] > -1:
        return binom[n][k]
    else:
        binom[n][k] = binomial(n - 1, k) + binomial(n - 1, k - 1)
        return binom[n][k]

# 2. 반복문을 활용한 DP 방식 (Bottom-up)
def binomial2(n,k):
    binom = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k) + 1): # j<=k and j<=i
            if j == 0 or i == j:
                binom[i][j] = 1
            else:
                binom[i][j] = binom[i-1][j-1] + binom[i-1][j]

    return binom[n][k]

