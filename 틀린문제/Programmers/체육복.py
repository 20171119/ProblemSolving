def solution(n, lost, reserve):
    # lost 이면서 reserve인 사람 제거 => 차집합 이용
    set_reserve = set(reserve)
    set_lost = set(lost)
    reserve = list(set_reserve - set_lost)
    lost = list(set_lost - set_reserve)
    answer = n - len(lost)
    
    # reserve를 기준으로 왼쪽부터 빌려줘야 최대가 됨
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
            answer += 1
        elif r+1 in lost:
            lost.remove(r+1)
            answer += 1
    return answer

# 다른사람 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)