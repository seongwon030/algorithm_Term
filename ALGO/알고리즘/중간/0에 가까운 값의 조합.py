from itertools import combinations

n = int(input())

A = list(map(int, input().split()))
k = int(input())

comb = list(combinations(A, k))

# 절댓값이 최소인 거 구하면 됨
min_sum = float('inf')
for i in comb:
    if abs(sum(i)) < min_sum:
        min_sum = sum(i)

print(min_sum)