# 분해합 브론즈2
n = int(input())

check = False
for i in range(1, n + 1):
    sum_list = list(map(int, str(i)))
    result = i + sum(sum_list)
    if result == n:
        print(i)
        check = True
        break
if not check:
    print(0)
