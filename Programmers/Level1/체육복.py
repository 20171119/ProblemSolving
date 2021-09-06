def solution(n, lost, reserve):
    answer = 0
    # 여분을 가진 학생 == 도난 당한 학생 => list 차집합 구글링 검색 - set 이용
    set_reserve = set(reserve)
    set_lost = set(lost)
    reserve = list(set_reserve - set_lost)
    lost = list(set_lost - set_reserve)
    # reserve를 기준으로 왼쪽 부터 빌려줘야 최대가 됨.
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    answer = n - len(lost)
    return answer