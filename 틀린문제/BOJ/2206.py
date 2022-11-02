# 골드4 벽 부수고 이동하기
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
# 3차원 행렬 visited[x][y][z] => z = 0 이라면 벽 파괴 가능 / z = 1 이라면 벽 한번 뚫은 상태
# 중간에 벽을 부순 경로는 벽을 안부순 경로만 이동 가능, 벽을 안부순 경로는 그 이후 벽을 한번 부술 경로로 이동 가능
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque([])
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0: # 벽이 아니고 한번도 방문 안했다면
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
                elif graph[nx][ny] == 1 and z == 0: # 벽이고 아직 벽 파괴를 사용하지 않았다면
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    q.appendleft((nx, ny, 1))
    return -1
print(bfs())