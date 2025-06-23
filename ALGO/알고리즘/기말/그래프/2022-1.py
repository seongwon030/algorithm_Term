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

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
print(*count_components(graph))
