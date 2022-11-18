# 실버5 그룹 단어 체커
n = int(input())
answer = 0
for _ in range(n):
    word = input()
    stack = []
    check = True
    for w in word:
        if w not in stack:
            stack.append(w)
        else:
            if stack[-1] == w:
                continue
            else:
                check = False
                break
    if check:
        answer += 1

print(answer)