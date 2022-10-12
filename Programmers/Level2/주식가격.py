from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        now = queue.popleft()
        time = 0
        for q in queue:
            time += 1
            if now > q:
                break
        answer.append(time)
        
    
    return answer