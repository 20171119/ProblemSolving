def solution(s):
    answer = 0
    for i in range(len(s)):
        if is_possible(rotate(s, i)):
            answer += 1
    return answer

def rotate(s, i):
    return s[i:] + s[:i]

def is_possible(s):
    stack = []
    for i in s:
        if i in ["[", "{", "("]:
            stack.append(i)
        else:
            if not stack:
                return False
            top = stack.pop()
            if i == "]" and top != "[":
                return False
            elif i == "}" and top != "{":
                return False
            elif i == ")" and top != "(":
                return False
    if stack:
        return False
    return True