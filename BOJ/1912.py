# 실버2 연속합
import sys
import copy
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = copy.deepcopy(arr)
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
print(max(dp))
