# 골드1 외판원 순회
def tsp(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (n-1)) - 1:
        if graph[i][0]:
            return graph[i][0]
        else:
            return INF

    min_route = INF

    for j in range(1, n):
        if not graph[i][j]:
            continue
        if route & (1 << j-1):
            continue
        D = graph[i][j] + tsp(j, route | (1 << (j-1)))
        if min_route > D:
            min_route = D
    
    dp[i][route] = min_route

    return min_route

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n-1) for _ in range(n)]
INF = int(1e9)

print(tsp(0,0))