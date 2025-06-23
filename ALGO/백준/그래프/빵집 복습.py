import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R,C = map(int, input().split())
bread = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dy = [-1, 0, 1]
answer = 0

def dfs(x, y):
    if y == C-1:
        return True
    for d in dy:
        nx = x + d
        ny = y + 1
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and bread[nx][ny] == '.':
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True
    return False

for i in range(R):
    if dfs(i,0):
        answer += 1

print(answer)