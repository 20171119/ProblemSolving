import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

INF = 1e9
distance = [INF] * (n+1)
distance[x] = 0

def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == INF:
                distance[i] = distance[now] + 1
                q.append(i)

bfs(x)

check = True
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = False

if check:
    print(-1)