# 골드5 평범한 배낭
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[0,0]]
bag = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = graph[i][0]
        v = graph[i][1]

        if w > j:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j], v + bag[i-1][j-w])

print(bag[n][k])