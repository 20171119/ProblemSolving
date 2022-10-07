from itertools import combinations

def solution(numbers):
    answer = []
    for comb in list(combinations(numbers, 2)):
        answer.append(sum(comb))
    answer = list(set(answer))
    answer.sort()
         
    return answer