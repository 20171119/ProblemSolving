# 실버5 집합
import sys

input = sys.stdin.readline


m = int(input())
S = []

for _ in range(m):
    command = input().split()
    if command[0] == "add":
        n = int(command[1])
        if n not in S:
            S.append(n)
    elif command[0] == "remove":
        n = int(command[1])
        if n in S:
            S.remove(n)
    elif command[0] == "check":
        n = int(command[1])
        if n in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        n = int(command[1])
        if n in S:
            S.remove(n)
        else:
            S.append(n)
    elif command[0] == "all":
        S = [i for i in range(1, 21)]
    elif command[0] == "empty":
        S = []
