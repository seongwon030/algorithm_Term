from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
k = int(input())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0,0,0))

visited = [[float('inf')] * n for _ in range(n)]
visited[0][0] = 0

while queue:
    x, y, rest_count = queue.popleft()

    if x == n-1 and y == n-1:
        if rest_count <= k:
            print(rest_count)
            exit()

    for i in range(4):
        for step in range(1, k+1):
            nx, ny = x + dx[i] * step, y + dy[i] * step
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 1:
                break

            if visited[nx][ny] > rest_count + 1:
                visited[nx][ny] = rest_count + 1
                queue.append((nx, ny, rest_count + 1))


