import sys
input = sys.stdin.readline

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        root[y_root] = x_root
        return True
    return False

n,m,k = map(int,input().split())
power_plants = list(map(int,input().split()))
edges = [list(map(int,input().split())) for i in range(m)]

root = [i for i in range(n+1)]

for i in range(1, len(power_plants)):
    union(power_plants[0], power_plants[i])

edges.sort(key=lambda x:x[2])
ans = 0

for a,b,w in edges:
    if find(a) != find(b):
        if find(a) in power_plants and find(b) in power_plants:
            continue
        union(a,b)
        ans += w

print(ans)