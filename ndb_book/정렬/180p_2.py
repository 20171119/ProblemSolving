n = int(input())
arr = []
for _ in range(n):
    name, grade = input().split()
    arr.append((name, int(grade)))

arr.sort(key=lambda x: x[1])
for name, grade in arr:
    print(name, end=' ')