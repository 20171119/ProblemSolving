# 실버4 덱
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    op = input().split()
    if len(op) == 2:
        if op[0] == "push_front":
            q.appendleft(int(op[1]))
        if op[0] == "push_back":
            q.append(int(op[1]))
    if len(op) == 1:
        if op[0] == "pop_front":
            print(-1) if not q else print(q.popleft())
        if op[0] == "pop_back":
            print(-1) if not q else print(q.pop())
        if op[0] == "size":
            print(len(q))
        if op[0] == "empty":
            print(1) if not q else print(0)
        if op[0] == "front":
            print(-1) if not q else print(q[0])
        if op[0] == "back":
            print(-1) if not q else print(q[-1])