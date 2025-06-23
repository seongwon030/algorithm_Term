def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                # 현재 경로에 다시 등장 => 사이클 존재
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

graph = {
    0: [1],
    1: [2],
    2: [0],  # 사이클 존재
    3: [4],
    4: []
}

print(has_cycle_directed(graph))  # 출력: True
