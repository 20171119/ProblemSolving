from string import ascii_lowercase, ascii_uppercase

def solution(s, n):
    answer = ''
    upper = list(ascii_uppercase)
    lower = list(ascii_lowercase)
    for i in s:
        if i in upper:
            idx = upper.index(i)
            answer += upper[(idx + n)%len(upper)]
        elif i in lower:
            idx = lower.index(i)
            answer += lower[(idx + n)%len(lower)]
        else:
            answer += " "
    return answer