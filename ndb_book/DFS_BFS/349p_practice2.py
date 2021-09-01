n = int(input())
data = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(index, num):
    global plus, minus, mul, div, max_val, min_val
    
    if index == n:
        max_val = max(max_val, num)
        min_val = min(min_val, num)

    if plus > 0:
        plus -= 1
        dfs(index + 1 , num + data[index])
        plus += 1
    
    if minus > 0:
        minus -= 1
        dfs(index + 1 , num - data[index])
        minus += 1
    
    if mul > 0:
        mul -= 1
        dfs(index + 1 , num * data[index])
        mul += 1
    
    if div > 0:
        div -= 1
        dfs(index + 1 , int(num/data[index]))
        div += 1

dfs(1, data[0])
print(max_val)
print(min_val)