import math

def solution(n, m):
    return [math.gcd(n,m), (n*m)//math.gcd(n,m)]

# 유클리드 호제법
def gcd(a, b):
    
    while b > 0:
        a, b = b, a % b 
    return a

def lcm(a, b):
    return a * b / gcd(a, b)