from itertools import permutations

def solution(n, weak, dist):
    # 둥근 외벽을 일자로 두배로 늘림
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 답을 최대 친구수 + 1 로 초기화시킴
    # weak를 모두 도는지 체크
    for start in range(length):
        # 친구들을 나열하는 모든 경우의 수를 하나씩 살펴봄
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 친구 수
            position = weak[start] + friends[count-1] # 해당 친구가 점검할 수 있는 최종 위치
            # 시작 점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할수있는 위치 벗어난 경우
                if position < weak[index]:
                    count += 1 # 친구 추가
                    if count > len(dist): # 친구수가 초과될 경우
                        break
                    position = weak[index] + friends[count-1] # 새로운 친구의 최종 위치
            answer = min(answer, count) 

    if answer > len(dist):
        return -1
    return answer