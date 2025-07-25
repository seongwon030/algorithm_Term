from collections import deque

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0,0,0))

# 최소 이동 횟수를 저장하는 리스트
visited = [[float('inf')] * n for _ in range(n)]
visited[0][0] = 0

while queue:
    x,y,rest_count = queue.popleft()

    if x == n-1 and y == n-1:
        print(rest_count)
        exit()

    for i in range(4):
        for step in range(1, k+1):
            nx, ny = x + dx[i] * step, y + dy[i] * step

            if nx < 0 or nx >= n or ny < 0 or ny >= n or maze[nx][ny] == 1:
                break
            # 지금까지 알고 있는 최소이동 횟수보다 rest_count+1이 더 작다면 갱신
            if visited[nx][ny] > rest_count + 1:
                visited[nx][ny] = rest_count + 1
                queue.append((nx, ny, rest_count + 1))

