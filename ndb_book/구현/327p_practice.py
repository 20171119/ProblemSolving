n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)] # 보드 생성
info = [] # 방향 정보
for _ in range(k):
    x, y = map(int, input().split())
    data[x][y] = 1 # 사과위치는  1로 설정

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c)) # 방향 설정

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방향 바꾸는 함수
def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 초기 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 있는 위치는 2로 설정
    direction = 0 # 뱀의 초기 방향 동쪽
    time = 0 # 총 시간
    index = 0 # info(방향 정보)의 인덱스
    q = [(x,y)] # 뱀이 차지하고 있는 위치정보 (꼬리가 앞)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 이동위치가 보드 안쪽이고 자기몸에 안 부딪혔을 때
        if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][ny] != 2:
            # 사과가 없을 때 -> 한칸 전진 후 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과 있을 때 -> 한칸 전진 후 꼬리 유지
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 부딪혔을 때
        else:
            time += 1
            break

        x, y = nx, ny # 뱀의 머리위치 수정
        time += 1 # 시간 증가
        # 시간이 방향전환 시간과 같을 때
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())