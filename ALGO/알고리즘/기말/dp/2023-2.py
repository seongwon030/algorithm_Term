def longest_adjacent_diff_one_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if abs(arr[i] - arr[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

with open("input2.txt") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

print(longest_adjacent_diff_one_subsequence(arr))
