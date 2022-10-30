# 골드5 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = int(1e5)
graph = [-1] * (MAX+1) # 목적지(인덱스)별 걸린 시간

def bfs():
    q = deque([n])
    graph[n] = 0
    while q:
        now = q.popleft()
        if now == k:
            return graph[now]
        for next in (now + 1, now - 1, now * 2):
            if 0 <= next <= MAX and graph[next] == -1:
                if next == now * 2: # 순간이동
                    q.appendleft(next) # 걸리는 시간 0초 이므로 최우선순위를 위해 appendleft
                    graph[next] = graph[now]
                else: # 걸을 때
                    q.append(next)
                    graph[next] = graph[now] + 1

print(bfs())