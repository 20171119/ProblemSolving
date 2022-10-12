from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(val, idx) for idx, val in enumerate(priorities)])
    priorities.sort()
    while True:
        val, idx = q.popleft()
        if priorities[-1] == val:
            answer += 1
            priorities.pop()
            if idx == location:
                break
        else:
            q.append((val, idx))
    return answer