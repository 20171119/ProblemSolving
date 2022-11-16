# 골드4 알파벳
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
history = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def dfs(x, y):
    global answer
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] not in history:
                history.add(graph[nx][ny])
                dfs(nx, ny)
                history.discard(graph[nx][ny])
    answer = max(answer, len(history))

history.add(graph[0][0])
dfs(0,0)
print(answer)