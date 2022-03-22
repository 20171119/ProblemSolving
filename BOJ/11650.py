# 좌표 정렬하기 실버5
import sys

N = int(sys.stdin.readline())
result = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    result.append((x, y))

result.sort(key=lambda x: (x[0], x[1]))

for x, y in result:
    print(x, y)
