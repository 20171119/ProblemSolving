# 막대기 브론즈2
import sys

n = int(sys.stdin.readline())
h_list = []
for _ in range(n):
    h_list.append(int(sys.stdin.readline()))

result = 0
now_h = 0
for i in range(len(h_list) - 1, -1, -1):
    if h_list[i] > now_h:
        result += 1
        now_h = h_list[i]

print(result)
