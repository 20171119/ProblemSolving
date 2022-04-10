# 실버3 모든순열
import sys

n = int(sys.stdin.readline())
result = []


def solve():
    if len(result) == n:
        print(" ".join(map(str, result)))
        return
    for i in range(1, n + 1):
        if not i in result:
            result.append(i)
            solve()
            result.pop()


solve()
