def solution(key, lock):
    answer = False
    global n, m
    m = len(key)
    n = len(lock)
    
    for i in range(2*n):
        for j in range(2*n):
            for k in range(4): # 키 90도 회전 4번
                key = rotate_key(key)
                if check_result(key, lock, i, j): # 키를 i, j 위치에 놓았을때 결과 확인
                    return True
    
    return answer

# 자물쇠랑 열쇠 결합 시 풀리는지 확인
def check_result(key, lock, row, col):
    # 열쇠를 한칸씩 아래, 오른쪽으로 옮기르모 전체 그리드를 3n X 3n 이라 생각하고 풀기
    grid = [[0]*(3*n) for _ in range(3*n)]
    
    # 그리드 정중앙에 자물쇠 위치
    for i in range(n):
        for j in range(n):
            grid[i+n][j+n] = lock[i][j]
    
    # 키를 그리드에 위치 시키기
    for i in range(m):
        for j in range(m):
            grid[row+i][col+j] += key[i][j]
    
    # 그리드 정중앙 자물쇠의 모든 값이 1인지 확인
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if grid[i][j] != 1:
                return False
    return True
    
    
# 키 90도 회전
def rotate_key(key):
    result = []
    for j in range(m):
        mid = []
        for i in range(m-1, -1, -1):
            mid.append(key[i][j])
        result.append(mid)
    return result
    