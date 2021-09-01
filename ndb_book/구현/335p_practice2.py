from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 둥근 외벽을 두배로 늘려 일자로 펼침
    for i in range(length):
        weak.append(weak[i] + n)
    # answer 을 최대 친구수 + 1 로 초기화 시킴
    answer = len(dist) + 1
    for start in range(length):
        # 친구 투입 경우의 수 체크
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 친구 수
            # 해당 친구가 끝까지 갈 수 있는 위치
            position = weak[start] + friends[count - 1]
            # 시작지점부터 모든 취약점에 대해서 체크
            for index in range(start, start + length):
                if position < weak[index]:
                    count = count + 1
                    if count > len(dist): # 더투입 불가능 하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer