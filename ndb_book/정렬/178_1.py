n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))
result.sort(reverse=True)
for r in result:
    print(r, end=" ")
