# 실버5 집합
# 집합 함수 기억하기 add, discard
import sys

input = sys.stdin.readline


m = int(input())
S = set()

for _ in range(m):
    command = input().split()
    if len(command) == 1:
        if command[0] == "all":
            S = set([i for i in range(1, 21)])
        else: 
            S = set()
    else:
        n = int(command[1])
        if command[0] == "add":
            S.add(n)
        elif command[0] == "remove":
            S.discard(n)
        elif command[0] == "check":
            if n in S:
                print(1)
            else:
                print(0)
        elif command[0] == "toggle":
            if n in S:
                S.discard(n)
            else:
                S.add(n)
