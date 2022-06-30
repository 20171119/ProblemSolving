n = int(input())
result = []
for _ in range(n):
    name, score = input().split()
    result.append([name, int(score)])

result.sort(key=lambda x: x[1])

for r in result:
    print(r[0], end=" ")
