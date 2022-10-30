# 골드4 숨바꼭질 4
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = int(1e5)
graph = [0] * (MAX + 1)
move = [0] * (MAX + 1)

def path(now):
    result = []
    temp = now
    for _ in range(graph[now]):
        result.append(temp)
        temp = move[temp]
    return ' '.join(map(str, result[::-1]))

def bfs(start):
    q = deque([start])
    graph[start] = 1    
    while q:
        now = q.popleft()
        if now == k:
            print(graph[now] - 1)
            print(path(now))
            return
        for next in (now-1, now+1, now*2):
            if next < 0 or next > MAX or graph[next] != 0:
                continue
            graph[next] = graph[now] + 1
            move[next] = now
            q.append(next)

bfs(n)