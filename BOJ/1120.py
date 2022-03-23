# 실버4 문자열
a, b = input().split()
b = list(b)

result = []
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    result.append(count)
print(min(result))
