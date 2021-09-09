#1. 위, 아래 알파벳 정할때 최소거리 구하기
#2. 오른쪽, 왼쪽 움직일때 최소거리 구히기
def solution(name):
    # 위, 아래 최소 (원래 AAA... 에서 name까지의 알파벳 거리 구함)
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    answer = 0
    print(change)
    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            return answer
        #오른쪽, 왼쪽 최소
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        #위치 조정
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer