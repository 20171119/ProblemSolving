from collections import Counter

def solution(nums):
    answer = 0
    dic = Counter(nums) # 포켓몬 번호: 포켓몬 개수
    keys = list(dic.keys())
    return len(keys) if len(nums) // 2 >= len(keys) else len(nums) // 2

# 다른 사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))