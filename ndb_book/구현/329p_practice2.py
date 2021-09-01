# 구조물 확인
def possible(answer):
    for frame in answer:
        x, y, stuff = frame
        if stuff == 0: # 기둥 일때
            # 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥위
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1: # 보 일때
            # 한쪽 끝이 기둥위 or 양쪽 끝이 보와 연결
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
            if not possible(answer): # 가능한지 확인
                answer.append([x,y,stuff]) # 다시 설치
        elif operate == 1: # 설치
            answer.append([x,y,stuff]) # 일단 설치
            if not possible(answer): # 가능한지 확인
                answer.remove([x,y,stuff]) # 삭제
        answer = sorted(answer)
    return answer

build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
n = 5

print(solution(n, build_frame))