n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

INF = 100000
dp = [INF] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(coins[i], m+1):
        if dp[j-coins[i]] != INF:
            dp[j] = min(dp[j], dp[j-coins[i]] + 1)

if dp[m] != INF:
    print(dp[m])
else:
    print(-1)