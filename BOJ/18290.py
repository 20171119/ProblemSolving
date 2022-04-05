# 실버1 NM과 K(1)
# 시간초과나고 어려웠음... 다시 풀기
N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = -1000000


def dfs(cx, cy, index, s):
    if index == K:
        global result

        if result < s:
            result = s
        return

    for x in range(cx, N):
        for y in range(cy if x == cx else 0, M):
            if visited[x][y]:
                continue
            flag = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if visited[nx][ny]:
                        flag = False
            if flag:
                visited[x][y] = True
                dfs(x, y, index + 1, s + board[x][y])
                visited[x][y] = False


dfs(0, 0, 0, 0)
print(result)
