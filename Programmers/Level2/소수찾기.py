import itertools

def is_prime_number(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)

    arrays = []
    for i in range(1, len(numbers)+1):
        for j in itertools.permutations(numbers, i):
            n = ''.join(j)
            arrays.append(int(n))
    arrays = list(set(arrays))
    for arr in arrays:
        if is_prime_number(arr):
            answer += 1

    return answer