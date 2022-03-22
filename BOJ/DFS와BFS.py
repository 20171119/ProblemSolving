# 1260번 실버2
# deque가 list 보다 push, pop이 압도적으로 빠름 O(1) <-> O(n) list
from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향

# 정점 번호 작은거 부터 방문
for g in graph:
    g.sort()

visitied = [False]*(n+1)
visitied1 = [False]*(n+1)
def dfs(graph, v, visitied):
    visitied[v] = True
    print(v, end=' ')
    for g in graph[v]:
        if not visitied[g]:
            dfs(graph, g, visitied)

def bfs(graph, start, visitied):
    q = deque([start])
    visitied[start] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for g in graph[cur]:
            if not visitied[g]:
                q.append(g)
                visitied[g] = True

dfs(graph, v, visitied)
print()
bfs(graph, v, visitied1)