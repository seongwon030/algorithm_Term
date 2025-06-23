import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        root[x] = y
        return True
    return False

n = int(input())
root = [i for i in range(n)]
w = [list(map(int, input().split())) for _ in range(n)]
edges = []

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        edges.append((i,j,w[i][j]))

edges.sort(key=lambda x:x[2])
total = 0

for i,j,dist in edges:
    if union(i,j):
        total += dist

print(total)