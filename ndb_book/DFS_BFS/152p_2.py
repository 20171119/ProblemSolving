from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
                if graph[next_x][next_y] == 1:
                    queue.append((next_x, next_y))
                    graph[next_x][next_y] += graph[x][y]


bfs(0, 0)
print(graph[n - 1][m - 1])
