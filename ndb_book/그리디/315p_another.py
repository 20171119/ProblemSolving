#combinations 이용
from itertools import combinations
n,m = map(int, input().split())
balls = list(map(int, input().split()))
coms = list(combinations(balls,2))
for com in coms:
  a, b = com
  if a == b:
    coms.remove((a,b))

print(len(coms))