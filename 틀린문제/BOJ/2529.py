# 실버2 부등호 - 10/18
# 순열 라이브러리를 통해 완탐으로 가능한 순서 모두 찾아서 해결 가능
# 아래 방법은 재귀 이용
def operate(n1, n2, sign):
    if sign == "<":
        return n1 < n2
    else:
        return n1 > n2

def dfs(count, num):
    if count == k+1:
        result.append(num)
        return
    for i in range(10):
        if visited[i]:
            continue
        if count == 0 or operate(num[-1], str(i), signs[count-1]):
            visited[i] = True
            dfs(count + 1, num + str(i))
            visited[i] = False

import sys
input = sys.stdin.readline
k = int(input())
signs = input().split()
result = []
visited = [False] * 10

dfs(0, "")
result.sort()
print(result[-1])
print(result[0])

