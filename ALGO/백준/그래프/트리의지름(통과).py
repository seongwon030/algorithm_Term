import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 아무거나 한 정점 잡고 거기서 제일 먼 노드 구함
# 그 노드에서 가장 먼 노드를 구함

def dfs(u, path):
    global diameter, leaf

    if diameter < path:
        diameter = path
        leaf = u

    visited[u] = 1

    for v,w in tree[u]:
        if visited[v] == 0:
            dfs(v, path+w)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,w = map(int, input().split())
    tree[a].append((b,w))
    tree[b].append((a,w))

diameter = 0
leaf = -1
visited = [0] * (n+1)
dfs(1,0)

visited = [0] * (n+1)
dfs(leaf, 0)
print(diameter)