# 골드5 토마토
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
answer = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    global answer
    q = deque([])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j, 0))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, time = q.popleft()
        answer = max(answer, time)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny, time+1))


bfs()
flag = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = False
            break

print(answer) if flag else print(-1)