from collections import deque
from itertools import permutations

def operate(n1, n2, op):
    if op == "+":
        return str(int(n1) + int(n2))
    elif op == "-":
        return str(int(n1) - int(n2))
    elif op == "*":
        return str(int(n1) * int(n2))

def calculate(exp, op):
    arr = deque([])
    temp = ""
    for i in exp:
        if i.isnumeric():
            temp += i
        else:
            arr.append(temp)
            temp = ""
            arr.append(i)
    if temp:
        arr.append(temp)
    for o in op:
        stack = deque([])
        while arr:
            now = arr.popleft()
            if now == o:
                stack.append(operate(stack.pop(), arr.popleft(), now))
            else:
                stack.append(now)
        arr = stack
    return abs(int(arr[0]))

def solution(expression):
    answer = 0
    operators = ["+", "-", "*"]
    for op in list(permutations(operators, 3)):
        answer = max(answer, calculate(expression, op))
    return answer