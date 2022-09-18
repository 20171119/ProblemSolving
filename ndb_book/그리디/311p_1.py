n = int(input())
fears = list(map(int, input().split()))

fears.sort()
result = 0
num = 0
for i in range(n):
    num += 1
    if fears[i] <= num:
        result += 1
        num = 0

print(result)