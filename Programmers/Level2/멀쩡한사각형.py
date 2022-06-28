import math


def solution(w, h):
    gcd = math.gcd(w, h)
    answer = w * h - (w + h - gcd)
    return answer
