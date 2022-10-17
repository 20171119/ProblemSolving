def solution(files):
    answer = []
    
    for file in files:
        num_idx, tail_idx = 0, 0
        for i in range(len(file)):
            if file[i].isnumeric() and num_idx == 0:
                num_idx = i
            if not file[i].isnumeric() and num_idx != 0:
                tail_idx = i
                break
        head = file[:num_idx]
        if tail_idx != 0:
            number = file[num_idx:tail_idx]
            tail = file[tail_idx:]
            answer.append((head, number, tail))
        else:
            number = file[num_idx:]
            answer.append((head, number))
    answer.sort(key = lambda x: (x[0].upper(), int(x[1])))
    result = []
    for a in answer:
        result.append(''.join(a))
    return result

# 다른사람 풀이
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0])) # number에 대한 정렬
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0]) # head에 대한 정렬
    return b