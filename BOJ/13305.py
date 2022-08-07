n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))
result = 0

c = costs[0]
for i in range(n-1):
    if c > costs[i]:
        c = costs[i]
    result += c * roads[i]

print(result)  