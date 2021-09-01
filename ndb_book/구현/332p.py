from itertools import combinations
n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

home_list = []
chicken_list = []
INF = 1e9

for x in range(n):
    for y in range(n):
        if city[x][y] == 1:
            home_list.append((x,y))
        if city[x][y] == 2:
            chicken_list.append((x,y))

# 모든 치킨집중 m 개의 치킨집 뽑는 조합 리스트
chickens_com = list(combinations(chicken_list, m))

# 치킨 거리 합 계산 함수
def get_sum(chickens):
    result = 0
    # 모든 집에 대하여
    for home in home_list:
        x, y = home
        temp = INF
        # 가장 가까운 치킨집 찾기
        for chicken in chickens:
            cx, cy = chicken
            temp = min(temp, (abs(x-cx) + abs(y-cy)))
        # 가장 가까운 치킨집 거리 더하기
        result += temp
    return result

result = INF
# 여러개의 조합 리스트중 계산
for chickens in chickens_com:
    result = min(result, get_sum(chickens))

print(result)