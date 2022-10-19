# 실버2 가장 긴 감소하는 부분 수열
# 가장 긴 증가하는 부분 수열 이용하기
# 배열 뒤집은 후 가장 긴 증가하는 오름차순 구하기
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.reverse()
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))