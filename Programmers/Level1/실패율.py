from collections import Counter

def solution(N, stages):
    answer = []
    
    total = len(stages)
    stages = Counter(stages) # 스테이지 번호 : 사람 수
    n2success = {}  # 스테이지 번호: 성공률
    
    for i in range(1, N+1):
        if total == 0:
            n2success[i] = 0
        else:
            n2success[i] = stages[i] / total
            total -= stages[i]
        
    arr = [(k,v) for k, v in n2success.items()]
    arr.sort(key=lambda x: (-x[1], x[0]))
    for i in arr:
        answer.append(i[0])
    return answer