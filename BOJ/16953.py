# 실버2 A->B
# bfs (bottom-up)
import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())

def bfs():
    q = deque([])
    q.append((a, 0))
    while q:
        now, count = q.popleft()
        if now == b:
            return count + 1
        elif now > b:
            continue
        else:
            if now * 2 <= b:
                q.append((now * 2, count + 1))
            if int(str(now) + '1') <= b:
                q.append((int(str(now) + '1'), count + 1))
    return -1
print(bfs())

# 그리디 방식 (top-down)
a,b = map(int,input().split())
r = 1
while(b!=a):
    r+=1
    temp = b
    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2
    
    if temp == b:
        print(-1)
        break
else:
    print(r)