# 날짜계산 실버5
E, S, M = map(int, input().split())
result = 1
e, s, m = 1, 1, 1
while True:
    if E == e and S == s and M == m:
        break

    if e + 1 != 15:
        e = (e + 1) % 15
    else:
        e = 15

    if s + 1 != 28:
        s = (s + 1) % 28
    else:
        s = 28

    if m + 1 != 19:
        m = (m + 1) % 19
    else:
        m = 19
    result += 1


print(result)
