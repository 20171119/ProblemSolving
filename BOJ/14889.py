# 실버2 스타트와 링크
from itertools import combinations

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

players = list(combinations([i for i in range(1, N + 1)], int(N / 2)))

result = 100000
for i in range(int(len(players) / 2)):
    start = players[i]
    link = players[len(players) - i - 1]
    a, b = 0
