import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def dfs(x, depth):
    calc[x] = True
    d[x] = depth
    for y in graph[x]:
        if calc[y]:
            continue
        parent[y] = x
        dfs(y, depth+1)

def lca(a,b):
    # depth 똑같이 맞추기
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 공통 조상 찾기
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

T = int(input())
for i in range(T):
    n = int(input())

    parent = [0] * (n+1)
    d = [0] * (n+1)
    calc = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(n - 1):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1,0)

    a,b = map(int, input().split())
    print(lca(a,b))