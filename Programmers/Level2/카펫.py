def solution(brown, yellow):
    answer = []
    all_num = brown + yellow #전체 칸의 개수 = 가로 길이 * 세로 길이
    for x in range(all_num, 2, -1):
        if all_num % x == 0: # x = 가로길이
            y = all_num / x # y = 세로길이 = 전체칸의 개수 / 가로길이
            if (x - 2) * (y - 2) == yellow: # 노란색 칸의 개수 = (가로길이 -2) * (세로길이 -2)
                answer.append(x)
                answer.append(y)
                break
    return answer