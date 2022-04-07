# 실버2 스타트와 링크
from itertools import combinations, permutations

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

players = list(combinations([i for i in range(1, N + 1)], int(N / 2)))

result = 100000
for i in range(int(len(players) / 2)):
    start = players[i]
    link = players[len(players) - i - 1]
    a, b = 0, 0
    for x, y in list(permutations(list(start), 2)):
        a += S[x - 1][y - 1]
    for x, y in list(permutations(list(link), 2)):
        b += S[x - 1][y - 1]
    result = min(result, abs(b - a))
print(result)
