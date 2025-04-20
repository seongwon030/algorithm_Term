import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input())

parent = [0] * (n+1)
d = [0] * (n+1)
calc = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    calc[x] = True
    d[x] = depth
    for y in graph[x]:
        if calc[y]:
            continue
        parent[y] = x
        dfs(y, depth+1)

def lca(a,b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1,0)

m = int(input())

for _ in range(m):
    a,b = map(int, input().split())
    print(lca(a,b))