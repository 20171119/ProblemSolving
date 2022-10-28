# 실버1 단지번호붙이기
from collections import deque


n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    global count
    if visited[x][y] or graph[x][y] == 0:
        return
    q = deque([])
    q.append((x,y))
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            count += 1
            q.append((nx, ny))

answer = []
for i in range(n):
    for j in range(n):
        count = 0
        if graph[i][j] != 0:
            bfs(i, j)
        if count != 0:
            answer.append(count)
answer.sort()
print(len(answer))
for a in answer:
    print(a)
