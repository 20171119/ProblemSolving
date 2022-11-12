# 골드3 아기상어
# 1. bfs를 통해 아기상어가 먹을 수 있는 물고기들의 후보를 거리, x, y 좌표 순으로 정렬
# 2. 후보 중 가장 우선순위로 이동시켜서 물고기 먹고나서 1번으로 돌아감
# 3. 먹을 후보가 없다면 정답 반환
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    visited = [[0] * n for _ in range(n)]
    result = []
    q = deque([])
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] <= size[0]:
                    if 0 < graph[nx][ny] < size[0]:
                        visited[nx][ny] = visited[x][y] + 1
                        result.append((visited[nx][ny] - 1, nx, ny))
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
    return sorted(result)

x, y, answer = 0, 0, 0
size = [2, 0]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

# 맨 앞의 후보만 먹으로 이동 후 다시 후보 탐색
while True:
    graph[x][y] = size[0]
    result = deque(bfs(x, y)) # 후보 bfs로 가져오기
    
    if not result:
        break
    
    # 맨앞의 후보를 먹으로 이동 후 먹기
    dist, nx, ny = result.popleft()
    answer += dist
    size[1] += 1

    # 상어의 크기가 커지는지 체크
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
    
    # 상어 이동
    graph[x][y] = 0
    x, y = nx, ny

print(answer)