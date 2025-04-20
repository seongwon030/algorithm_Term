def dfs(x, y, steps):
    global cnt

    if x < 0 or x >= n or y < 0 or y >= n or maze[x][y] == 1:
        return

    if x == n-1 and y == n-1:
        if steps <= k:
            cnt += 1
        return

    maze[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        dfs(nx, ny, steps+1)

    maze[x][y] = 0


n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

dfs(0,0,0)
print(cnt)