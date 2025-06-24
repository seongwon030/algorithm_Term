with open ("input2.txt", "r") as f:
    n,k = map(int,f.readline().split())

    graph = [[0]*n for _ in range(n)]

    for i in range(n):
        first,second = map(int,f.readline().split())
        graph[i][first] = 1
        graph[first][i] = 1
        graph[i][second] = 1
        graph[second][i] = 1

    for i in range(n):
        graph[i][i] = 0

    for i in range(n):
        for j in range(n):
            print(graph[i][j],end = " ")
        print()

def count_components(graph):
    n = len(graph)
    visited = [False] * n
    result = []

    def dfs(v):
        count = 1
        visited[v] = True
        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                count += dfs(i)
        return count

    for i in range(n):
        if not visited[i]:
            component_size = dfs(i)
            result.append(component_size)

    return result

print(len(count_components(graph)))

INF = float('inf')

dist = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
        elif graph[i][j]:
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 결과 출력
for i in range(n):
    for j in range(n):
        print(-1 if dist[i][j] == INF else dist[i][j], end=' ')
    print()