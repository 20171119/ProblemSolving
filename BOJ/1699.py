# 실버2 제곱수의 합
import sys
input = sys.stdin.readline

n = int(input())
INF = 100000
if n <=2 :
    print(n)
else:
    dp = [INF] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        for j in range(1, i):
            if i < j * j:
                break
            dp[i] = min(dp[i], dp[i - j*j] + 1)
    print(dp[n])