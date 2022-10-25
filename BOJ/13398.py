# 골드5 연속합 2
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# dp[0][i]: 특정 원소 제거 안한 경우, dp[1][i]: 특정 원소를 제거한 경우
dp = [[0] * n for _ in range(2)]

if n > 1:
    dp[0][0] = arr[0]
    answer = -int(1e9)
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
        answer = max(answer, dp[0][i], dp[1][i])
    print(answer)
else:
    print(arr[0])