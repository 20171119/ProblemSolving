from itertools import combinations
n = int(input()) # 복도의 크기
board = [] # 복도 정보
teacher = [] # 모든 선생님의 위치 정보
space = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teacher.append((i,j))
        # 장애물 설치할 수 있는 위치 젖아
        if board[i][j] == 'X':
            space.append((i,j)) 

# 특정 방향으로 감시 진행 (학생 발견:True, 미발견: False)
def watch(x, y, direction):
    # 왼쪽
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    # 오른쪽
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # 위쪽
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    # 아래쪽
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1     

# 장애물 설치 후 한명이라도 감지되는지 검사
def process():
    # 모든 선생님 위치를 하나씩 확인
    for x,y in teacher:
        # 4가지 방향으로 검사
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

find = False

# 빈 공간에서 3개의 장애물을 설치할 모든 조합 확인
for data in combinations(space, 3):
    for x,y in data:
        board[x][y] = 'O'
    # 학생이 한명도 발견되지 않았을 때
    if not process():
        find = True
        break
    for x,y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")
        

    
