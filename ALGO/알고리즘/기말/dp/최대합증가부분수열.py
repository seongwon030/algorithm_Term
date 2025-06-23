def max_sum_increasing_subsequence(A):
    n = len(A)
    dp = A[:]

    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + A[i])

    return max(dp)

A = list(map(int, input().split()))
print(max_sum_increasing_subsequence(A))
