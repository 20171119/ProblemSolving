# 골드5 암호만들기
from itertools import combinations

L, C = map(int, input().split())
alphabets = list(map(str, input().split()))
alphabets.sort()
aeiou = ["a", "e", "i", "o", "u"]

for comb in list((combinations(alphabets, L))):
    flag = False
    n = 0
    for c in comb:  # 모음 최소 1개, 자음 최소 2개 체크
        if c in aeiou:
            flag = True
        else:
            n += 1
    if not flag or n < 2:  # 모음이 하나도 없을때 or 자음이 2개 미만일 때
        continue
    result = "".join(comb)
    print(result)
