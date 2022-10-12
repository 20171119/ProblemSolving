def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0