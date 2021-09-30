def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1]) # 나간 지점순으로 오름차순 정렬
    camera = -30001
    for route in routes:
        if camera < route[0]: # 카메라 이후에 들어온 차량
            answer += 1
            camera = route[1] # 나갈때 시점으로 카메라 설치
    return answer