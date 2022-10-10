def solution(n):
    answer = [[0 for _ in range(i)] for i in range(1, n+1)]
    
    r, c = -1, 0
    num = 1
    for i in range(n):
        for j in range(n-i):
            if i % 3 == 0: # 아래 방향
                r += 1
            elif i % 3 == 1: # 오른쪽 방향
                c += 1
            elif i % 3 == 2: # 위쪽 방향
                r -= 1
                c -= 1
                
            answer[r][c] = num
            num += 1
    return sum(answer, [])