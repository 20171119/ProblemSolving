from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    length = len(q1)
    sum1, sum2 = sum(q1), sum(q2)
    if sum1 == sum2:
        return 0
    
    total = sum1 + sum2
    if total % 2 != 0:
        return -1
    for i in q1:
        if i > total // 2:
            return -1
    for i in q2:
        if i > total // 2:
            return -1
    
    while sum1 != sum2:
        if answer > length * 4: # q1과 q2가 완저히 원소를 바꿨다가 다시 돌아가는데 드는 횟수 - 이 이상 하면 의미 없다
            return -1
        while sum1 < sum2:
            n = q2.popleft()
            sum2 -= n
            sum1 += n
            q1.append(n)
            answer += 1
        while sum1 > sum2:
            n = q1.popleft()
            sum2 += n
            sum1 -= n
            q2.append(n)
            answer += 1
    return answer