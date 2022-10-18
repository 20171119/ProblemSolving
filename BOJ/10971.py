# 실버2 외판원 순회2
# TSP 문제
def dfs(start, next, cost, count):
    global result
    if count == n:
        if graph[next][start] != 0:
            result = min(result, cost + graph[next][start])
        return
    
    for i in range(n):
        if visited[i] or i == start or graph[next][i] == 0:
            continue
        visited[i] = True
        dfs(start, i, cost + graph[next][i], count + 1)
        visited[i] = False


import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [False] * n
result = int(1e9)

for i in range(n):
    dfs(i, i, 0, 1)
print(result)

