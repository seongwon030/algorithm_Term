def solve(k, count, i):
    if i == n:
        return count + 1
    elif A[i] < K:
        count += 1
        i += 1
        return solve(k, count, i)
    i += 1
    return solve(k, count, i)

n = int(input())
A = list(map(int, input().split()))
K = int(input())

count = 0
i = 0

solve(K, count, i)
print(count)