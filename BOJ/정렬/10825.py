# 국영수 실버4
# 더 좋은 정렬 방법 result.sort(key = lambda x : (-x[1] , x[2],-x[3],x[0]) )
import sys

n = int(sys.stdin.readline())

result = []
for _ in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    result.append((name, kor, eng, math))

result.sort(key=lambda x: str(x[0]))
result.sort(key=lambda x: int(x[3]), reverse=True)
result.sort(key=lambda x: int(x[2]))
result.sort(key=lambda x: int(x[1]), reverse=True)

for i in result:
    print(i[0])
