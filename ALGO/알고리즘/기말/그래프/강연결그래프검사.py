# 1. 임의의 정점 s를 선택해 s에서 출발하는 BFS/DFS 수행하여 정점 s에서 다른
#   모든 정점으로 가는 경로가 있는 지 확인

# 2. 그래프 G의 모든 간선들의 방향을 뒤집은 그래프를 Gc라고 할 때, Gc에서 다시
#    s에서 출발하는 BFS/DFS 수행하여 다른 모든 정점으로 가는 경로가 있는 지 검사.

# 3. 만약 다른 모든 정ㅈ머으로 가는 경로가 존재한다면, 원래 그래프 G에서
#    다른 모든 정점에서 s까지 가는 경로가 존재한다.

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n):
    data = list(map(int, input().split()))
    from_node = data[0]
    edge_node = data[1]
    for to_node in data[2:2+edge_node]:
        graph[from_node].append(to_node)

def is_reachable(graph, start):
    n = len(graph)
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                dfs(i)

    dfs(start)
    return all(visited)

def reverse_graph(graph):
    n = len(graph)
    reversed_graph = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            reversed_graph[v].append(u)
    return reversed_graph

reversed_graph = reverse_graph(graph)
strongly_connected = [False] * n

for i in range(n):
    if is_reachable(graph, i) and is_reachable(reversed_graph, i):
        strongly_connected[i] = True

if all(strongly_connected):
    print("YES")
else:
    print("NO")