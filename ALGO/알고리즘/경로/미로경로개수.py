# 상수 정의
PATHWAY_COLOUR = 0  # 지나갈 수 있는 길
WALL_COLOUR = 1     # 벽
PATH_COLOUR = 2     # 현재 지나가는 경로 표시

# 예시 미로 (0 = 길, 1 = 벽)
maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

N = len(maze)

def count_maze_paths(x, y):
    # 범위를 벗어나거나 벽이거나 이미 방문한 경우
    if x < 0 or y < 0 or x >= N or y >= N or maze[x][y] != PATHWAY_COLOUR:
        return 0

    # 출구에 도달한 경우 → 경로 1개
    if x == N - 1 and y == N - 1:
        return 1

    # 현재 위치 방문 표시
    maze[x][y] = PATH_COLOUR

    # 상하좌우 이동
    count = 0
    count += count_maze_paths(x - 1, y)  # 위
    count += count_maze_paths(x, y + 1)  # 오른쪽
    count += count_maze_paths(x + 1, y)  # 아래
    count += count_maze_paths(x, y - 1)  # 왼쪽

    # 백트래킹: 방문 해제
    maze[x][y] = PATHWAY_COLOUR

    return count

# 실행
total_paths = count_maze_paths(0, 0)
print("출구까지 가능한 경로 수:", total_paths)
