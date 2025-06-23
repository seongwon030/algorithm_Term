import heapq
import sys

input = sys.stdin.readline

v,e = map(int, input().split())
start_vertex = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])

def dijkstra(start,size):
    distance = [float('inf')] * (size+1)
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist: # 이미 더 짧은 거리로 갱신된 노드
            continue
        for n,w in graph[node]: # 인접 노드 체크
            cost = dist + w # 현재 노드까지의 가중치 + 인접 노드로 가는 가중치
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q,[cost,n])

    return distance

d = dijkstra(start_vertex,v)

for i in range(1,v+1):
    if d[i] == float('inf'):
        print('INF')
    else:
        print(d[i])
