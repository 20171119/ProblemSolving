def solution(numbers):
    arr = [str(n) for n in numbers]
    arr.sort(key=lambda x: 3*x, reverse=True)
    return str(int(''.join(arr)))