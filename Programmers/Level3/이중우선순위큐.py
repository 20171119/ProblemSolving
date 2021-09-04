#힙
import heapq

def solution(operations):
    answer = []
    q = []
    for operation in operations:
        c, d = operation.split()
        if c == 'I':
            d = int(d)
            heapq.heappush(q, d)
        elif c == 'D':
            if len(q) >= 1:
                if d == '1':
                    q.pop() # heapq pop 하는 메소드에서 최댓값을 하는게 구글링해도 안나와서 list에서 pop하는 것처럼 함
                elif d == '-1':
                    heapq.heappop(q)
    
    if len(q) >= 2:
        answer.append(max(q))
        answer.append(min(q))
    else:
        answer.append(0)
        answer.append(0)
        
    return answer