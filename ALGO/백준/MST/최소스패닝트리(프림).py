import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 프림: 아직 방문하지 않은 정점 중에서 가장 비용이 적은 간선을 선택하여 확장
# 비용이 적은 간선 찾기 위해서 모든 간선을 일일이 검색하는 것 : O(E)
# 최소 힙: O(log E)
V,E = map(int,input().split())

visited = [0] * (V+1)
graph = [[] for i in range(V+1)]

for i in range(E):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))

cnt = 0
ans = 0
q = []
heappush(q,(0,1))

while q:
    if cnt == V:
        break
    value, vertex = heappop(q)
    if not visited[vertex]:
        visited[vertex] = 1
        cnt += 1
        ans += value
        for i in graph[vertex]:
            heappush(q,i)

print(ans)
