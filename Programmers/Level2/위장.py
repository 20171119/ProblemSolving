from collections import Counter

def solution(clothes):
    answer = 1
    c = Counter([kind for name, kind in clothes]) # 의상 종류: 의상 개수
    arr = list(c.values())
    for i in range(len(arr)):
        answer = answer * (arr[i]+1) # 모든 경우의 수 = 각 의상별 개수 + 1(안입을 때) 을 계속 곱하고 마지막 -1 (모두 안입을떄)
                    
    return answer-1
#다른 사람 풀이
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer