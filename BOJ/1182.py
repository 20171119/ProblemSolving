# 실버2 부분수열의 합
import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for k in range(1, n+1):
    for comb in list(combinations(arr, k)):
        if sum(comb) == s:
            result += 1

print(result)