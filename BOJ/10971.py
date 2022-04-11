# 실버2 외판원 순회2
# TSP 문제
import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
result = 10000000


def solve(start, next, temp, visited):
    global result

    if len(visited) == N:
        if board[next][start] != 0:
            result = min(result, temp + board[next][start])
        return

    for i in range(N):
        if i != start and board[next][i] != 0 and i not in visited:
            visited.append(i)
            solve(start, i, board[next][i] + temp, visited)
            visited.pop()


for i in range(N):
    solve(i, i, 0, [i])

print(result)
