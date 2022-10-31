# 골드4 알고스팟
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs():
    q = deque([])
    q.append((0,0,0))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    graph[0][0] = -1
    while q:
        x, y, count = q.popleft()
        if x == n-1 and y == m-1:
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != -1:
                if graph[nx][ny] == 1:
                    q.append((nx, ny, count + 1))
                else:
                    q.appendleft((nx, ny, count))
                graph[nx][ny] = -1
    return count

print(bfs())