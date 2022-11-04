# 골드5 강의실 배정
# 1. 현재 회의실에서의 회의가 끝나는 시간보다 다음 회의의 시작시간이 빠르면 회의실을 하나 추가로 개설한다.
# 2. 현재 회의실에서 회의가 끝나는 시간보다 다음 회의의 시작시간이 느리면 현재 존재하는 회의실에서 이어서 회의 개최가 가능하다.
import heapq

n = int(input())
q = []
for _ in range(n):
    s, t = map(int, input().split())
    q.append([s,t])

q.sort()
room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]: # 다음회의 시작시간이 현재회의 종료시각보다 빠르다면
        heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
    else: # 현재회의에서 개최 가능
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])