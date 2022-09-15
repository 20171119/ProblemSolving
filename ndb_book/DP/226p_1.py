n, m = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

INF = 9999999
dp = [INF] * (m+1)
dp[0] = 0

for coin in coins:
    for j in range(coin, m+1):
        if dp[j-coin] != INF:
            dp[j] = min(dp[j], dp[j-coin] + 1)

if dp[m] == INF:
    print(-1)
else:
    print(dp[m])


