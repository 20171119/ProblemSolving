# 브론즈1
weight = int(input())
count = 0
num5 = weight // 5
flag = True
for i in range(num5, -1, -1):
    check_weight = weight - (5 * i)
    if check_weight % 3 == 0:
        j = check_weight // 3
        count = i + j
        print(count)
        flag = False
        break

if flag:
    print(-1)
