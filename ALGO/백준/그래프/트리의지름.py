import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(u, path):
    global diameter

    if diameter < path:
        diameter = path

    visited[u] = 1

    for v,w in tree[u]:
        if visited[v] == 0:
            dfs(v, path+w)

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    a,b,w = map(int, input().split())
    tree[a].append((b,w))
    tree[b].append((a,w))

    parent[a] = 1

diameter = 0

leaf = []

for i in range(1,n+1):
    if parent[i] == 0:
        leaf.append(i) # 리프노드

visited = [0] * (n+1)
dfs(leaf[0], 0)

for i in range(1, len(leaf)):
    visited = [0] * (n + 1)
    for j in range(i):
        visited[leaf[j]] = 1
    dfs(leaf[j], 0)

print(diameter)