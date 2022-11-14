# 골드4 빙산
# 빙산이 두 덩어리 이상인지 확인하기
# 두덩어리가 아니라면 빙산 녹이기
import sys
from collections import deque
import copy
input = sys.stdin.readline

def get_count():
    def bfs(x, y):
        q = deque([])
        q.append((x,y))
        visited[x][y] = True

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

    count = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                count += 1
    return count

def reduce():
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        if new_graph[i][j] > 0:
                            new_graph[i][j] -= 1
    return new_graph


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0
while True:
    count = get_count()
    if count == 0:
        print(0)
        break
    if count >= 2:
        print(answer)
        break
    graph = reduce()
    answer += 1

# 다른사람 풀이
# https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2573-%EB%B9%99%EC%82%B0-BFS
