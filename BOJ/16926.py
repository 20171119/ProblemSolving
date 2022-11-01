# 실버1 배열 돌리기 1
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def rotate():
    temp = [[0] * m for _ in range(n)]
    for i in range(min(n, m) // 2):
        x, y = i, i # 시작 x, y
        val = arr[x][y] # 이전 값 저장
        # 좌
        for j in range(i+1, n-i):
            x = j
            temp[x][y] = val
            val = arr[x][y]
        # 하
        for j in range(i+1, m-i):
            y = j
            temp[x][y] = val
            val = arr[x][y]
        # 우
        for j in range(i+1, n-i):
            x = n - j - 1
            temp[x][y] = val
            val = arr[x][y]

        # 상
        for j in range(i+1, m-i):
            y = m - j - 1
            temp[x][y] = val
            val = arr[x][y]
    return temp

for _ in range(r):
    arr = rotate()

for i in arr:
    print(*i)