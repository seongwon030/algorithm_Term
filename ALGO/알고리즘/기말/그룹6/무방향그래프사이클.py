def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # 방문했는데 부모가 아니면 사이클
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1): # 초기 호출 시 부모가 없음을 나타내기 위한 임시값
                return True
    return False

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

print(has_cycle(graph))  # 출력: True
