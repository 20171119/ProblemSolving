# 로직이 많이 복잡한듯 함.. (블로그 참고)
# 대기하는 디스크 중 소요되는 시간이 가장 짧은 디스크 부터 처리하면 최소가 됨
import heapq

def solution(jobs):
    answer = 0
    now, i = 0, 0 # 현재 시점, 처리 한 작업 수
    start = -1 # 이전 작업 요청 시간
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            # 현재 시점 처리 가능한 작업인지 판단 조건
            # 이전 작업 요청시간 < 작업 요청 시간 <= 현재 시점
            if start < j[0] <= now: 
                heapq.heappush(heap, [j[1], j[0]]) #작업 소요시간 기준으로 정렬해야 되기때문에 먼저 넣어줌
        if len(heap) > 0: # 작업을 처리 중일때
            current = heapq.heappop(heap) # 작업 소요시간이 최소인 작업 heappop
            start = now 
            now += current[0] # 현재 시점 += 작업 소요 시간
            answer += (now - current[1]) # 소요시간 += 현재시점 - 작업 요청 시간
            i += 1 # 작업 처리 개수 + `1
        else: # 아무 작업도 없을 때
            now += 1 # 현재시점 +1
    return int(answer / len(jobs)) # 평균 시간