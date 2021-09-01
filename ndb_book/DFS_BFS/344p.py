from collections import deque

n, k = map(int, input().split())
graph = [] # 전체 보드정보
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 바이러스 정보
virus_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y)
            virus_list.append((graph[i][j], 0, i, j))
virus_list.sort() # 정렬 (낮은 번호부터 증식하므로)

target_s, target_x, target_y = map(int, input().split())

# 4방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()
queue = deque(virus_list)

while queue:
    num, time, x, y = queue.popleft()
    if time == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = num
                queue.append((num, time + 1, nx, ny))

print(graph[target_x-1][target_y-1])