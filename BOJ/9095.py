# 실버3 1,2,3 더하기
# 점화식 이용 - F(n) = F(n-1) + F(n-2) + F(n-3)
def get_count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return get_count(n - 1) + get_count(n - 2) + get_count(n - 3)


T = int(input())
for _ in range(T):
    n = int(input())
    print(get_count(n))
