def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0: #기둥
            # 바닥위 or 보의 한쪽 끝부분 or 다른 기둥 위
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1: # 보
            # 한쪽 끝 기둥 or 양쪽 끝 다른보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0: # 삭제
            answer.remove([x,y,stuff]) # 일단 삭제
            if not possible(answer): # 구조물 가능한지 확인
                answer.append([x,y,stuff]) # 다시 설치

        if operate == 1: # 설치
            answer.append([x,y,stuff]) # 일단 설치
            if not possible(answer): # 구조물 가능한지 확인
                answer.remove([x,y,stuff]) # 다시 삭제
        print(answer)
    return sorted(answer)
