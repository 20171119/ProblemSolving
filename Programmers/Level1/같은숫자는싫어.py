def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
        if answer[-1] == a:
            continue
        answer.append(a)
    return answer

# 다른 사람 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a