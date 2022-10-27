# 실버2 연결 요소의 개수
# union-find
def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(a, b):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

for i in range(1, n+1):
    parent[i] = find_parent(i, parent)
print(len(set(parent[1:])))

# dfs
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(idx):
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        answer += 1
        dfs(i)
print(answer)