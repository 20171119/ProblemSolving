def solution(priorities, location):
    answer = 0
    idx_p = []
    for idx in range(len(priorities)):
        idx_p.append((idx, priorities[idx])) # (idx, val) 값으로 저장
    priorities.sort()
    while True:
        idx, pri = idx_p.pop(0)
        if pri == max(priorities):
            priorities.pop()
            answer += 1
            if idx == location:
                return answer
        else:
            idx_p.append((idx, pri))