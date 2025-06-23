import sys
input = sys.stdin.readline

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
root = [i for i in range(n+1)]
points = [tuple(map(float,input().split())) for i in range(n)]

edges = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        x1,y1 = points[i]
        x2,y2 = points[j]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        edges.append((dist, i, j))

edges.sort()
total = 0

for dist, i, j in edges:
    if union(i,j): # 두 정점이 서로소 집합인 경우
        total += dist

print(f"{total:.2f}")