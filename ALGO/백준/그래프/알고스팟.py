import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    dist[0][0] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if dist[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft([nx,ny])
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])

bfs(0,0)
print(dist[m-1][n-1])