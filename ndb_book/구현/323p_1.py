def solution(s):
    answer = len(s)
    
    for n in range(1, len(s)//2 + 1): # 1부터 문자열의 절반까지 완전탐색
        answer = min(answer, compress_string(s, n))
    return answer

def compress_string(s, n):
    c = 1
    result = ""
    q = len(s)//n
    r = len(s)%n
    for i in range(0, q):
        start = i * n
        if s[start:start+n] == s[start+n:start+2*n]:
            c += 1
        else:
            if c != 1:
                result += str(c)
            result += s[start:start+n]
            c = 1
    if r != 0:
        result += s[len(s)-r:] # 남은 문자 추가
    return len(result)