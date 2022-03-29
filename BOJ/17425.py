# 골드5 약수의 합
# 17427 이랑 똑같은데 테스트케이스 추가때문에 시간초과남
# 미리 모든 약수의 누적합을 계산해 놓는 방식 dp
import sys

MAX = 1000000
dp = [1] * (MAX + 1)
sum = [0] * (MAX + 1)

for i in range(2, MAX + 1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1

for i in range(1, MAX + 1):
    sum[i] = sum[i - 1] + dp[i]

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(sum[N])
