# BOJ 10828 실버4
# input 으로 입력값 받으면 시간초과남...
# sys 를 이용할 것!!!!

import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    result = sys.stdin.readline().split()  # split 기억하기 !
    command = result[0]

    if command == "push":  # push 일 때
        stack.append(result[1])
    else:
        if command == "pop":
            if len(stack) == 0:
                print("-1")
            else:
                print(stack.pop())
        elif command == "size":
            print(len(stack))
        elif command == "empty":
            if len(stack) == 0:
                print("1")
            else:
                print(0)
        elif command == "top":
            if len(stack) == 0:
                print("-1")
            else:
                print(stack[len(stack) - 1])
        else:
            print("input ")
