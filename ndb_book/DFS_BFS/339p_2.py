import sys
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# 거리를 -1 로 초기화 하여 미방문 처리
distance = [-1] * (n+1)
distance[x] = 0

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[now] + 1

bfs(x)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
            