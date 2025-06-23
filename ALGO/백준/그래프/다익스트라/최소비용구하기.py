import heapq
from collections import defaultdict
import sys

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

v1,v2 = map(int, input().split())

distance = [INF] * (n+1)

def dijkstra(start):
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

dijkstra(v1)
print(distance[v2])