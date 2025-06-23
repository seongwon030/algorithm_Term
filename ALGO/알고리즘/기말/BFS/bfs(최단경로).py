from collections import deque

def bfs_v2(graph, start):
    d = {v: -1 for v in graph}
    pi = {v: None for v in graph}

    d[start] = 0
    pi[start] = None

    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if d[v] == -1:  # 아직 방문 안 했음
                d[v] = d[u] + 1
                pi[v] = u
                queue.append(v)

    return d, pi

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs_v2(graph, 'A'))