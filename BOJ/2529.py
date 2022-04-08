# 실버2 부등호
from sys import stdin

input = stdin.readline


def check_sign(n1, sign, n2):
    if sign == "<":
        return n1 < n2
    else:
        return n1 > n2


def solve(depth, temp):
    global MIN, MAX

    if depth == n + 1:
        MIN = min(MIN, int(temp))
        MAX = max(MAX, int(temp))
        return
    for i in range(10):
        if visited[i]:
            continue
        if depth == 0 or check_sign(int(temp[-1]), sign[depth - 1], i):
            visited[i] = True
            solve(depth + 1, temp + str(i))
            visited[i] = False


n = int(input())
sign = input().split()
MIN, MAX = 9999999999, -9999999999
visited = [False] * 10
solve(0, "")
print(str(MAX))
if len(str(MIN)) < n + 1:
    print("0" + str(MIN))
else:
    print(str(MIN))
