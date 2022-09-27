from itertools import combinations

INF = 1e9
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

chickens = [] # 모든 치킨집의 좌표
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append((i,j))

homes = [] # 모든 집의 좌표
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            homes.append((i, j))


# 치킨집이 정해졌을 때 집과 치킨 사이의 모든 거리
def get_sum(chickens):
    result = 0
    for home in homes:
        temp = INF
        hx, hy = home
        for chicken in chickens:
            cx, cy = chicken
            temp = min(temp, abs(hx-cx) + abs(hy-cy)) # 집과 여러개의 치킨 집중 가장 가까운 치킨집 거리 구하기
        result += temp
    return result

result = INF
for combs in list(combinations(chickens, m)): # 조합을 이용해 m개의 가능한 치킨집 모두 고르기
    result = min(result, get_sum(combs))

print(result)
    
