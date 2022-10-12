from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        cur = heappop(scoville)
        _next = heappop(scoville)
        result = cur + _next * 2
        heappush(scoville, result)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer