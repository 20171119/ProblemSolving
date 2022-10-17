def solution(s):
    arr = s.split()
    result = ""
    for a in arr:
        for i in range(len(a)):
            if i % 2 == 0:
                result += a[i].upper()
            else:
                result += a[i].lower()
    idx = 0
    for i in range(len(s)):
        if s[i].isalnum():
            s = s[:i] + result[idx] + s[i+1:]
            idx += 1
            
    return  s

# 다른 사람 풀이
def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))