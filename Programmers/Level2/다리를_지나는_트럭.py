from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_in = deque(truck_weights) # 다리 건너기 전 트럭
    truck_out = deque([]) # 다리를 건넌 트럭
    bridge = deque([0 for _ in range(bridge_length)]) # 다리에 있는 트럭
    total = 0 # 다리에 있는 트럭 무게 총 합
    while len(truck_out) != len(truck_weights):
        out = bridge.popleft()
        total -= out
        if out > 0:
            truck_out.append(out)
        
        if total + truck_in[0] <= weight:
            truck = truck_in.popleft()
            truck_in.append(0)
            bridge.append(truck)
            total += truck
        else:
            bridge.append(0)
            
        answer += 1
    return answer