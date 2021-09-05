# 나올수 있는 수 모두 구하기 - 파이썬 순열 라이브러리 이용
# 그리고 소수 판별
import itertools
import math

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        #''.join 안쓰니까 튜플 형태로 나옴. => 여기서 헤멤
        perlist = list(map(''.join, itertools.permutations(list(numbers), k)))
        for i in list(set(perlist)): # 중복되는수 set 으로 줄임.
            if check_prime(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer

# 소수 판별 함수 - 2 ~ n의 제곱근 +1 보다 작은 수로 나누어지면 소수
def check_prime(n):
    k = math.sqrt(n)
    if n < 2: 
        return False
    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True