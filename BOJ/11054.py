# 골드4 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

increase = [1] * n
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            increase[i] = max(increase[i], increase[j] + 1)

a.reverse()
decrease = [1] * n
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
decrease.reverse()

answer = 0
for i in range(n):
    answer = max(answer, increase[i] + decrease[i])
print(answer - 1)
