# pop을 이용하면 계쏙 효율성 deque 이용했지만 remove 쓸시 또 0점
# 아예 pop이랑 remove 이용안하고 인덱스만 건드는 방법으로 품
# people 정렬 후 왼쪽 값을 뽑은 후, 오른쪽부터 boat 최대값 안넘는 인덱스를 찾음.

def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    
    if left == right: # 마지막 한사람 남았을 때
        answer += 1
    
    return answer