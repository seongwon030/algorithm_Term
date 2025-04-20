n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

found = 0

def countPath(x,y, turn, prev_dir):
    global found

    if x < 0 or x >= n or y < 0 or y >= n or maze[x][y] == 1:
        return

    if x == n-1 and y == n-1:
        if turn <= k:
            found = True
            return

    maze[x][y] = 1
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if prev_dir == -1 or prev_dir == dir:
            countPath(nx, ny, turn, dir)
        else:
            countPath(nx, ny, turn+1, dir)

    maze[x][y] = 0

countPath(0,0,0, -1)

print("Yes" if found else "No")

