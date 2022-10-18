# 실버1 NM과 K(1) - 10/18
# 완탐했다가 시간초과 난 문제, 백트랙킹을 통해 오른쪽과 아래로만 이동하도록 하기
def dfs(px, py, count, total):
    global answer
    if count == k:
        answer = max(answer, total)
        return

    # 오른쪽과 아래로만 이동하도록 하기
    for x in range(px, n): # 행 아래부터 이동
        for y in range(py if x==px else 0, m): # 같은 행이면 해당 열부터 오른쪽으로 이동
            if visited[x][y]:
                continue

            flag = False
            for i in range(4): # 상,하,좌,우 방문했는지 확인
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >=m:
                    continue
                if visited[nx][ny]:
                    flag = True
                    break
            
            if not flag: # 방문 안했다면
                visited[x][y] = True
                dfs(x, y, count + 1, total + graph[x][y])
                visited[x][y] = False


import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
answer = -1e9

dfs(0, 0, 0, 0)
print(answer)
