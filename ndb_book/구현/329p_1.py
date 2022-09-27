def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1: # 설치
            answer.append([x, y, a])
            if not possible(answer):
                answer.pop()
        else: # 삭제
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer

def possible(answer):
    for frame in answer:
        x, y, a = frame
        if a == 0: # 기둥
            if y == 0: # 바닥 위에 있을 때
                continue
            else:
                if [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer: # 다른 기둥 위에 있거나 보 위에 있을 때
                    continue
                else:
                    return False
        else: # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer: # 한쪽 끝 부분이 기둥위에 있을 때
                continue
            else:
                if [x-1, y, 1] in answer and [x+1, y, 1] in answer: # 양쪽 끝 부분이 보 일때
                    continue
                else:
                    return False
    return True