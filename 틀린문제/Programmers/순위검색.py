from itertools import combinations
from bisect import bisect_left
from collections import defaultdict

def solution(info, query):
    answer = []
    dic = defaultdict(list) # 조건: [점수]
    for i in info:
        i = i.split()
        conditions = i[:-1]
        score = int(i[-1])
        for i in range(5):
            for comb in list(combinations([0, 1, 2, 3], i)): # "-" 를 포함한 모든 경우의 수
                temp = conditions[:]
                for i in comb:
                    temp[i] = "-"
                key = "".join(temp)
                dic[key].append(score)
    
    for k, v in dic.items():
        v.sort()
    
    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        
        target_key = "".join(q[:-1])
        target_score = int(q[-1])
        count = 0
        if target_key in dic:
            scores = dic[target_key]
            idx = bisect_left(scores, target_score)
            count = len(scores)-idx
        answer.append(count)
        
    return answer