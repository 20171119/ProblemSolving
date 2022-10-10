def solution(s):
    answer = []
    arr = []
    for i in list(s[2:-2].split("},{")):
        arr.append(i.split(","))
    arr.sort(key=lambda x:len(x))
    for a in arr:
        result = list(set(a) - set(answer))[0]
        answer.append(result)
    return [int(i) for i in answer]

# 다른사람 풀이 (정규표현식, Counter)
import re
from collections import Counter

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))