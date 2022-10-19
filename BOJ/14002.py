# 골드4 가장 긴 증가하는 부분 수열 4
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

order = max(dp)
result = []
for i in range(n-1, -1, -1):
    if order == dp[i]:
        order -= 1
        result.append(a[i])
result.reverse()
print(*result)