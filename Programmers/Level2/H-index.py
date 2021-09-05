# 위키백과 보고 이해함.
def solution(citations):
    answer = 0
    citations.sort(reverse=True) # 내림 차순 정렬
    for i in range(len(citations)):
        if citations[i] < i+1: # 논문 개수가 인덱스보다 작을때, 그 전의 인덱스 값을 리턴
            break
        answer = i + 1
    return answer