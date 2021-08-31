#스택/큐
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)] # bridge 초기 값 0으로 설정
    bridge_sum = 0 #원래 sum()함수 이용했다가 5번에서 시간초과 되서 변수활용
    while bridge:
        answer += 1
        out_truck = bridge.pop(0) # bridge를 벗어나는 트럭
        bridge_sum -= out_truck
        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight:
                in_truck = truck_weights.pop(0) # bridge를 들어오는 트럭
                bridge_sum += in_truck
                bridge.append(in_truck)
            else:
                bridge.append(0)

    return answer
