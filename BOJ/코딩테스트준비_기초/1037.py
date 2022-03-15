# 실버5 약수
n = int(input())
divisor = list(map(int, input().split()))
divisor.sort()
if len(divisor) == 1:
    print(divisor[0] * divisor[0])
else:
    print(divisor[0] * divisor[len(divisor)-1])
