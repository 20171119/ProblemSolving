# 브론즈2 일곱 난쟁이
from itertools import combinations

dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

combs = list(combinations(dwarfs, 7))

for comb in combs:
    if sum(comb) == 100:
        result = list(comb)
        result.sort()
        break

for r in result:
    print(r)
