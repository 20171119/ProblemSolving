# 실버4 큐
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([])
for _ in range(n):
    op = input().split()
    if len(op) == 1:
        if op[0] == "pop":
            print(q.popleft()) if q else print(-1)
        if op[0] == "size":
            print(len(q))
        if op[0] == "empty":
            print(1) if not q else print(0)
        if op[0] == "front":
            print(q[0]) if q else print(-1)
        if op[0] == "back":
            print(q[-1]) if q else print(-1)
    else:
        q.append(int(op[1]))