n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if graph[x][y] == 1:
        return

    graph[x][y] = 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return 1


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == 1:
            result += 1

print(result)
