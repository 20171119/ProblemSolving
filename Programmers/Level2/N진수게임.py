def solution(n, t, m, p):
    answer = ''
    s = ""
    number = 0
    while len(s) <= t * m:
        for i in parse(number, n):
            s += i
        number += 1
        
    idxs = [i*m + (p-1) for i in range(t)]
    for idx in idxs:
        answer += s[idx]
    return answer

def parse(num, n):
    alpha = ["A", "B", "C", "D", "E", "F"]
    result = ""
    if num == 0:
        return "0"
    
    while num > 0:
        num, mod = divmod(num, n)
        if mod >= 10: # 10진수 이상의 수라면
            result += alpha[mod % 10]
        else:
            result += str(mod)
    return result[::-1]