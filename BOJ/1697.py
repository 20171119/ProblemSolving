# 실버1 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * (100001)

def bfs(n, k):
    q = deque([])
    q.append((n, 0))
    dx = [1, -1]

    while q:
        loc, time = q.popleft()
        if loc == k:
            return time
        visited[loc] = True
        
        # 걸을 때
        for i in range(2):
            nx = loc + dx[i]
            if nx < 0 or nx > 100000:
                continue
            if visited[nx]:
                continue
            q.append((nx, time+1))
        
        # 순간이동 할 때
        nx = loc * 2
        if nx >= 0 and nx <= 100000:
            q.append((nx, time+1))

print(bfs(n, k))