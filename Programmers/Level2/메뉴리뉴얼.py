import string
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    total_list = []
    for order in orders: # orders에서 조합 가능한 코스요리 경우의수 모두 찾기
        order = list(order)
        order.sort()
        for i in range(2, len(order) + 1):
            for comb in list(combinations(order, i)):
                total_list.append("".join(comb))
    
    total_list.sort()
    dic = Counter(total_list) # 코스요리: 개수
    for c in course:
        result = []
        for key, val in dic.items():
            if len(key) == c:
                result.append((val, key))
        result.sort(reverse=True)
        if result:
            max_count = result[0][0]
            if max_count >= 2:
                for c, s in result:
                    if c == max_count:
                        answer.append(s)
                    else:
                        break
    answer.sort()
    return answer

# 나와 알고리즘은 같은데 깔끔한 풀이
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]