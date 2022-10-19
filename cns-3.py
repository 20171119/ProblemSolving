def solution(string):
    answer = []
    def cut(s, num, n ,time): # 자른 문자열, 숫자, 정답, 순열 수
        if num >= 99999: # 6자리 이상이면
            answer.append(n)
            return
        if s[:len(str(num + 1))] == str(num + 1):
            cut(s[len(str(num + 1)):], num + 1, n + len(str(num + 1)), time + 1)
        elif time > 1:
            answer.append(n)
    for i in range(len(string)):
        for j in range(1, 6):
            cut(string[i + j:], int(string[i:i+ j]) , j, 1)
    return max(answer)

print(solution("98991001013"))
print(solution("9999899999100000"))
print(solution("01020304"))

# ex) 9899100 -> 7
# i = 0, j = 2
# cut(991001013, 98, 2, 1)
# cut(1001013, 99, 4, 2)
# cut(1013, 100, 7, 3)
# cut(3, 100, 10, 4) => 10
# 문자열이 주어질때 오름차순이 되는 가장 긴 문자열 길이