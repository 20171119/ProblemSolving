from itertools import combinations

n, m = map(int, input().split())
weights = list(map(int, input().split()))

result = 0
for a, b in list(combinations(weights, 2)):
    if a != b:
        result += 1

print(result)