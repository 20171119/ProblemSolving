# 실버1 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline

# 8방향
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [-2, 2, -1, 1, -2, 2, -1, 1]

def bfs(x, y, target_x, target_y):
    q = deque([])
    q.append((x,y))
    graph[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == target_x and y == target_y:
            return graph[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != 0:
                continue
            q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    graph = [[0] * n for _ in range(n)]

    print(bfs(x, y, target_x, target_y))