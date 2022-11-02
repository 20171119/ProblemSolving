# 실버2 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx,ny)


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                answer += 1
    print(answer)