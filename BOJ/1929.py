# 실버3 소수구하기
# 소수구하기 그대로하면 시간초과
# 소수 구할떄 배수들은 제외하도록
M, N = map(int, input().split())
check = [0] * (N + 1)

for i in range(2, N + 1):
    if check[i] == 0:
        if i >= M:
            print(i)
        for j in range(i * 2, N + 1, i):
            if check[j] == 0:
                check[j] = 1