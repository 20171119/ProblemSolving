from itertools import permutations

def solution(n, weak, dist):
    answer = 0
    length = len(weak) # 원래 취약점 개수
    # 둥근 외벽 일자로 펴기
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    
    for start in range(length): # 취약점 시작 지점
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 친구 수
            position = weak[start] + friends[count-1] # 친구의 외벽 점검 종료 위치
            for index in range(start, start+length): # 취약점 모두 점검
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    
    return answer