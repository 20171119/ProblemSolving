# 실버1 안전 영역
def bfs(x, y):
    q = deque([])
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_val = 1

for i in range(n):
    for j in range(n):
        max_val = max(max_val, graph[i][j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

for h in range(max_val+1):
    visited = [[False] * n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= h:
                visited[i][j] = True
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                result += 1
                bfs(i, j)
    answer = max(result, answer)

print(answer)
