from itertools import combinations

n = int(input())
team = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

ans = 0

teams = [i for i in range(0, n)]
combs = list(combinations(teams, k))
max_list = []

for comb in combs:
    sum = 0
    for j in range(n):
        if j not in comb:
            continue
        for k in range(n):
            if k not in comb:
                continue
            sum += team[j][k]

    max_list.append(sum)

print(max(max_list))