# 아마 시간초과
from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))
result = []

for i in range(1,n+1):
    for data in list(combinations(coins, i)):
        result.append(sum(data))

result = list(set(result))
for i in range(1,1000001):
    if i not in result:
        print(i)
        break

# 답지 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1 # 현재 상태가 target-1 까지의 금액을 만들수 있다는 의미
for x in data:
  if target < x: # 현재 화페로 target 금액을 만들 수 없다면
    break 
  target += x # 현재 화폐로 target 금액을 만들 수 있다면 업데이트
print(target)
