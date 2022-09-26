from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    # 큐가 빌때 까지
    while q:
        x, y = q.popleft()
        # 상, 하, 좌, 우 비교
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로를 벗어난다면
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽이라면 무시
            if graph[nx][ny] == 0:
                continue

            # 방문하지 않았으면거 갈 수 있는 길이라면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0,0))
    