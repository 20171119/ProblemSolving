def solution(s):
    zero, count = 0, 0
    while s != "1":
        count += 1
        zero += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
    return [count, zero]