def dfs(x,y,isbombed):
    global count

    if x < 0 or x >= n or y < 0 or y >= n or maze[x][y] == 1:
        return

    if x == n-1 and y == n-1:
        if isbombed <= k:
            count += 1
        return

    temp = maze[x][y]
    maze[x][y] = 1

    if temp == 2:
        isbombed += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        dfs(nx, ny, isbombed)

    maze[x][y] = temp # 0이든 2든 기존 상태 기억 후 다시 백트래킹

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

dfs(0,0,0)
if count:
    print('yes')
else:
    print('no')