# 실버 3 N과 M(1)
import sys
input = sys.stdin.readline
def dfs(n, m):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return 
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(n, m)
            result.pop()
            visited[i] = False

N, M = map(int, input().split())
visited = [False] * (N+1)
result = []
dfs(N, M)
