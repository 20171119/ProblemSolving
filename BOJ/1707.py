# 골드4 이분 그래프
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global flag
    q = deque([])
    q.append(start)
    if visited[start] == 0:
        visited[start] = 1
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                if visited[now] == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
                q.append(i)
            else:
                if visited[now] == visited[i]:
                    flag = False
                    return

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    flag = True
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, v+1):
        bfs(i)
    
    if flag:
        print("YES")
    else:
        print("NO")
