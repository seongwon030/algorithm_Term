IMAGE_COLOR = 1
ALREADY_COUNTED = 2

N = 8
grid = [
   [1,0,0,0,0,0,0,1],
    [0,1,1,0,0,1,0,0],
    [1,1,0,0,1,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,1,0,1,0,1,0,0],
    [0,1,0,1,0,1,0,0],
    [1,0,0,0,1,0,0,1],
    [0,1,1,0,0,1,1,1],
]

def countCells(x, y):
    if x < 0 or x >= N or y < 0 or y >= N or grid[x][y] != IMAGE_COLOR:
        return 0

    grid[x][y] = ALREADY_COUNTED

    return (1 +
        countCells(x - 1, y) +  # 위
        countCells(x + 1, y) +  # 아래
        countCells(x, y - 1) +  # 왼쪽
        countCells(x, y + 1))   # 오른쪽

print(countCells(1, 1))
