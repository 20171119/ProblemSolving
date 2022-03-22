#15686번 골드5
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

chickens_com = list(combinations(chicken_list, m))

def get_sum(chickens):
    result = 0
    for home in home_list:
        x, y = home
        temp = INF
        for chicken in chickens:
            cx, cy = chicken
            d = min(temp, (abs(x-cx) + abs(y-cy)))
            temp = d
        result += d
    return result

result = INF
for chickens in chickens_com:
    result = min(result, get_sum(chickens))

print(result)