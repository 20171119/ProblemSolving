# 실버2 로또
import sys
from itertools import combinations

input = sys.stdin.readline
while True:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break
    S.pop(0)

    for comb in list(combinations(S, 6)):
        for i in comb:
            print(i, end=" ")
        print()
    print()
