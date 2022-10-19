# 실버2 1,2,3 더하기 5
import sys
input = sys.stdin.readline

t = int(input())
dp = [[0, 0, 0] for _ in range(100001)]
# 1, 2, 3 으로 끝날 떄의 경우의 수
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    # i가 1로 끝날떄의 경우의 수 = i-1이 2 or 3 으로 끝날때의 수
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    # i가 2로 끝날떄의 경우의 수 = i-2이 1 or 3 으로 끝날때의 수
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    # i가 3로 끝날떄의 경우의 수 = i-3이 1 or 2 으로 끝날때의 수
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % 1000000009)