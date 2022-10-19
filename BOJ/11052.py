# 실버1 카드 구매하기
import sys
input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = cards[i]
    for k in range(1, i):
        dp[i] = max(dp[i], cards[k] + dp[i-k])
print(dp[n])