# 실버3 화살표 그리기
N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
points.sort(key=lambda x: (x[1], x[0]))


def check_point(a, b):
    if a < 0 or b >= N or points[a][1] != points[b][1]:
        return False
    else:
        return True


result = 0
INF = 10000000000
for i in range(N):
    temp = INF
    if check_point(i - 1, i):
        temp = min(temp, points[i][0] - points[i - 1][0])
    if check_point(i, i + 1):
        temp = min(temp, points[i + 1][0] - points[i][0])
    if temp != INF:
        result += temp
print(result)
