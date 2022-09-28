def solution(n):
    answer = ''
    s = "수박"
    for i in range(n):
        index = i%2
        answer += s[index]
    return answer