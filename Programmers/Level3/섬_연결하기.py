# 크루스칼 알고리즘 이용하기 (최소비용 연결 + 사이클 x)
# 크루스칼 알고리즘 블로그 참고함.
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준 오름차순 정렬
    connect = set([costs[0][0]]) # 연결을 확인하는 집합
    
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect: # 두 섬 모두 connect에 있다면
                continue
            if cost[0] in connect or cost[1] in connect: # 두 섬중 하나만 connect에 있다면
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer