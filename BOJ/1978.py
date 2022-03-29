# 실버4 소수 찾기
def check_prime(n):
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True


N = int(input())
nums = list(map(int, input().split()))
result = 0

for num in nums:
    if check_prime(num):
        result += 1
print(result)
