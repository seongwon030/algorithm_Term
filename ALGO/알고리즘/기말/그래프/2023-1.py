import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, u = heapq.heappop(pq) # 우선순위 큐에서 현재 가장 짧은 정점 u 꺼냄
        if cost > dist[u]:
            continue
        for v in range(n):
            if graph[u][v] != -1:
                new_cost = cost + graph[u][v]
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
    return dist

def count_components_and_find_diameters(graph):
    n = len(graph)
    visited = [False] * n
    components = []

    def dfs(v, component):
        visited[v] = True
        component.append(v)
        for i in range(n):
            if graph[v][i] != -1 and not visited[i]:
                dfs(i, component)

    for i in range(n): # 연결된 정점끼리 나누기
        if not visited[i]:
            component = []
            dfs(i, component)
            components.append(component)

    diameters = []

    for comp in components:
        # 1. 아무 점에서 시작해 가장 먼 점 찾기
        dist_from_any = dijkstra(graph, comp[0])
        u = max(comp, key=lambda x: dist_from_any[x])

        # 2. u에서 다시 먼 점 v 찾기
        dist_from_u = dijkstra(graph, u)
        v = max(comp, key=lambda x: dist_from_u[x])
        diameter = dist_from_u[v]

        diameters.append((u,v,diameter))

    return components, diameters

with open('input1.txt') as f:
    n, m = map(int, f.readline().split())
    graph = [[-1] * n for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, f.readline().split())
        graph[a][b] = c
        graph[b][a] = c

    for i in range(n):
        graph[i][i] = 0

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()

components, diameters = count_components_and_find_diameters(graph)
print(len(components))

max_diameter = 0
for u,v,d in diameters:
    if d > max_diameter:
        max_diameter = d

print(max_diameter)

