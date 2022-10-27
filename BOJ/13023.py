# 골드5 ABCDE
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
answer = False
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(number, depth):
    global answer
    visited[number] = True
    if depth == 4:
        answer = True
        return
    
    for i in graph[number]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if answer:
        print(1)
        break
if not answer:
    print(0)