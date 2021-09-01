n = int(input())
data = []
for _ in range(n):
    a, b = input().split()
    data.append((a,int(b)))
data.sort(key = lambda x:x[1])

for i in range(n):
    print(data[i][0], end=' ')