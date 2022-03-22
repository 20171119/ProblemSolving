#3190번 골드5
n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
board = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1 # 사과가 있는 곳은 1로 표시
l = int(input()) # 방향전환 수
info = [] # 방향전환 배열
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 방향 -> (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(c, direction):
    if c == 'D': #오른쪽 회전
        direction = (direction + 1) % 4
    else: # 왼쪽회전
        direction = (direction - 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    board[x][y] = 2 # 뱀이 있는 위치는 2로 설정
    direction = 0 # 방향 인덱스(처음 동)
    time = 0 # 총 소요 시간
    q = [(x,y)] # 뱀이 위치하는 곳
    index = 0 # 방향전환 인덱스

    while True:
        # 일단 뱀의 머리 이동
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 머리 이동한 곳이 보드의 바깥쪽이거나 자기 몸에 부딪혔을 경우 (자기 몸은 2로 표시)
        if nx<1 or nx>n or ny<1 or ny>n or board[nx][ny] == 2:
            time = time + 1
            break
        # 보드 안쪽이고 자기몸에 안부딪혔을 경우
        # 사과를 먹었다면
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            q.append((nx,ny))
        # 사과를 먹지 않았다면
        else:
            board[nx][ny] = 2
            q.append((nx,ny))
            px, py = q.pop(0) # 꼬리 제거
            board[px][py] = 0 

        x, y = nx, ny # 뱀의 머리 수정
        time = time + 1 # 시간 증가
        # 방향 전환 시간일 경우
        if index < l and time == info[index][0]:
            direction = turn(info[index][1], direction)
            index = index + 1
    return time

print(simulate())