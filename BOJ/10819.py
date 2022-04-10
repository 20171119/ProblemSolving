# 실버2 차이를 최대로
import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

arr, result = [], []
visited = [False] * n


def solve(depth):
    if depth == n:
        result.append(sum(abs(arr[i] - arr[i + 1]) for i in range(n - 1)))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(a[i])
            solve(depth + 1)
            visited[i] = False
            arr.pop()


solve(0)
print(max(result))
