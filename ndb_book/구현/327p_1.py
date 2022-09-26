from collections import deque

n = int(input())
k = int(input())
graph = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
for _ in range(k):
    x, y = map(int, input().split()) # 사과의 x, y 좌표
    graph[x][y] = 1 # 사과 1 로 표시
l = int(input())
directions = []
for _ in range(l):
    x, c = input().split()
    directions.append([int(x), c])

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L": # 왼쪽으로 회전 시
        direction = (direction + 1) % 4
    else: # 오른쪽으로 회전 시
        direction = (direction - 1) % 4
    return direction

def simulate():
    time = 0
    x, y = 1, 1 # 뱀의 머리
    graph[x][y] = 2 # 뱀이 위치하는 곳은 2로 표시
    q = deque()
    q.append((x,y)) # 뱀의 몸 전체를 기록하는 큐 / 맨앞은 꼬리
    idx = 0 # 방향배열의 인덱스
    direction = 0 # 방향, 처음에는 동쪽

    while True:
        # 이동할 x,y
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx < 1 or nx > n or ny < 1 or ny > n or graph[nx][ny] == 2: # 맵을 벗어나거나 자신의 몸에 부딪힌다면
            time += 1
            break
        else:
            if graph[nx][ny] != 1: # 사과가 없다면
                graph[nx][ny] = 2
                q.append((nx, ny))
                tx, ty = q.popleft() # 꼬리 부분 제거
                graph[tx][ty] = 0
            else:
                graph[nx][ny] = 2
                q.append((nx, ny))
        
        time += 1
        x, y = nx, ny # 머리 업데이트
        if idx < l and time == directions[idx][0]: # 방향을 바꿀 시간이라면
            direction = turn(direction, directions[idx][1])
            idx += 1
    return time

print(simulate())
