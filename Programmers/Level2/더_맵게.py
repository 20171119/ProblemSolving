import heapq # 파이썬 우선순위 큐

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트를 heap으로 변경
    while scoville[0] < K and len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new = min1 + min2 * 2
        heapq.heappush(scoville, new)
        answer += 1
    
    if scoville[0] < K:
        return -1
    
    return answer