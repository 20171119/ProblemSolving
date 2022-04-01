# 카잉 달력 실버1
def get_K(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


T = int(input())
result = []
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(get_K(M, N, x, y))
