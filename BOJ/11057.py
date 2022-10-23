# 실버1 오르막 수
import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 10 # 끝자리 수가 0~9 일때 가능한 모든 경우의 수

for i in range(n-1):
    for j in range(1,10):
        dp[j] += dp[j-1]
print(sum(dp) % 10007)