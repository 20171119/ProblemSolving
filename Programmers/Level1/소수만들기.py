from itertools import combinations
import math

def solution(nums):
    answer = 0
    for combs in list(combinations(nums, 3)):
        if is_prime(sum(combs)):
            answer += 1
    
    return answer

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True