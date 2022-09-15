n = int(input())
k = list(map(int, input().split()))

dp = [0] * 100
dp[0] = k[0]
dp[1] = max(k[0], k[1])

for i in range(2, n):
    dp[i] = max(k[i] + dp[i-2], dp[i-1])
print(dp[n-1])