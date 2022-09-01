from collections import deque
import sys 

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

distance = [-1] * (n + 1) # 방문안했을떄는 거리를 -1 로 하여 구분
distance[x] = 0

def bfs():
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                q.append(i)

bfs()

check = False
for idx, d in enumerate(distance):
    if d == k:
        check = True
        print(idx, end=' ')

if check == False:
    print(-1)