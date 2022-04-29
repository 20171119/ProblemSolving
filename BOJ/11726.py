# 실버3  2xn 타일링
import sys

input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n + 1)]

if n <= 3:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n] % 10007)
