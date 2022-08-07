n, W = map(int, input().split())
costs = []
for _ in range(n):
    costs.append(int(input()))

coin_num = 0
for i in range(n-1):
    if costs[i] < costs[i+1] and coin_num == 0:
        coin_num = W // costs[i]
        W -= costs[i] * coin_num
    elif costs[i] > costs[i+1] and coin_num != 0:
        W += costs[i] * coin_num
        coin_num = 0

W += costs[n-1] * coin_num
print(W)