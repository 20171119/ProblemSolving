# 실버5 최대공약수와 최소공배수
n1, n2 = map(int, input().split())


def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


def lcm(n1, n2):
    return int(n1 * n2 / gcd(n1, n2))


print(gcd(n1, n2))
print(lcm(n1, n2))
