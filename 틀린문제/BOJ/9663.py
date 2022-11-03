# 골드4 N-Queen
n = int(input())
row = [0] * n # 인덱스 i 번째 행에 몇 열에 위치하는지 정보
result = 0

def is_possible(x): # x행에 퀸 배치한게 가능한지
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 같은 열 혹은 대각선에 있다면 불가능
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i # x행 i열에 퀸 배치
            if is_possible(x): # x행에 퀸 배치한게 가능하다면
                dfs(x+1) # 다음행으로 이동
dfs(0)
print(result)