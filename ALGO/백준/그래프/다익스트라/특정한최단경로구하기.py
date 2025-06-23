import heapq
import sys

input = sys.stdin.readline

n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2 = map(int, input().split())

def dijkstra(start,size):
    distance = [float('inf')] * (size+1)
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n,w in graph[node]:
            cost = dist + w
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q,[cost,n])

    return distance

d1 = dijkstra(1,n) # 1번에서 모든 노드까지 거리
d2 = dijkstra(v1,n) # v1에서 모든 노드까지 거리
d3 = dijkstra(v2,n) # v2에서 모든 노드까지 거리

# 경로 1: 1 -> v1 -> v2 -> n
# d1[v1] : 1 -> v1
# d2[v2] : v1 -> v2
# d3[n] : v2 -> n

# 경로 2 : 1 -> v2 -> v1 -> n
# d1[v2] : 1 -> v2
# d3[v1] : v2 -> v1
# d2[n] : v1 -> n

result = min(d1[v2]+d2[n]+d3[v1], d1[v1]+d2[v2]+d3[n])

if result == float('inf'):
    print(-1)
else:
    print(result)