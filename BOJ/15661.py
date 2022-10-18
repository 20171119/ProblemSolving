# 골드5 링크와 스타트
# 완탐 방식과 dfs 방식으로 부분집합들을 모두 구할 수 있음
from itertools import combinations, permutations

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

all = [i for i in range(1, N + 1)]
result = 100000
for k in range(1, int(N//2) + 1):
    for players in list(combinations(all, k)):
        start = list(players)
        link = list(set(all) - set(players))
        a, b = 0, 0
        for x, y in list(permutations(list(start), 2)):
            a += S[x - 1][y - 1]
        for x, y in list(permutations(list(link), 2)):
            b += S[x - 1][y - 1]
        result = min(result, abs(b - a))
print(result)

# dfs를 통해 부분집합을 구하여 푼 풀이
# 골드5 링크와 스타트
def dfs(target):
    if target == n:
        score()
        return

    visited[target] = True
    dfs(target + 1)
    visited[target] = False
    dfs(target + 1)


def score():
    global result
    start, link = 0, 0
    for i in range(n-1):
        for j in range(i+1, n): # 조금이나마 포문을 줄이기 위해 중복을 제거함
            if visited[i] and visited[j]:
                start += s[i][j] + s[j][i]
            elif not visited[i] and not visited[j]:
                link += s[i][j] + s[j][i]
    result = min(result, abs(start-link))

import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = 100 * 20

dfs(0)
print(result)