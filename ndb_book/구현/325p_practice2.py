# 90도 회전한 matrix
def rotate_matrix_90_degree(a):
    m = len(a)
    n = len(a[0])
    result = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][m-1-i] = a[i][j]
    return result

# 자물쇠가 풀렸는지 check (자물쇠가 모두 1이되면 풀림)
def check(new_lock):
    length = len(new_lock) // 3
    for i in range(length, 2 * length):
        for j in range(length, 2 * length):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]# 3배 크기의 새로운 자물쇠를 만듬
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 90도 회전 계속하면서 검사
    for rotate in range(4):
        key = rotate_matrix_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                # key 더해줌
                for i in range(m):
                    for j in range(m):
                       new_lock[x+i][y+j] += key[i][j] 
                # check
                if check(new_lock):
                    return True
                # key 다시 빼줌
                for i in range(m):
                    for j in range(m):
                       new_lock[x+i][y+j] -= key[i][j] 
    return False
