# 골드4 이모티콘
import sys
from collections import deque
input = sys.stdin.readline

s = int(input())
visited = dict()
visited[(1,0)] = 0 # {(모니터 이모티콘 개수, 클립 이모티콘 개수): 총 시간}

def bfs():
    q = deque([]) # [(모니터 개수, 클립 개수)]
    q.append((1,0))
    while q:
        m, c = q.popleft()
        if m == s:
            print(visited[(m, c)])
            return
        # 1. 화면에 있는 이모티콘 클립보드에 모두 복사
        if (m, m) not in visited.keys():
            visited[(m,m)] = visited[(m, c)] + 1
            q.append((m, m))
        # 2. 클립보드에 있는 이모티콘 화면에 붙여넣기
        if m+c <= s and (m+c, c) not in visited.keys():
            visited[(m+c, c)] = visited[(m, c)] + 1
            q.append((m+c, c))
        # 3. 화면에 있는 이모티콘 중 하나 삭제
        if m-1 >= 0 and (m-1, c) not in visited.keys():
            visited[(m-1, c)] = visited[(m,c)] + 1
            q.append((m-1, c))

bfs()
print(visited)