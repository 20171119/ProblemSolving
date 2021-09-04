#정렬
# x*3 idea 참고 (못풀었음...)
def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key = lambda x: x*3, reverse = True)
    # x*3 => 각 문자열 마다 3번 반복
    # [3, 30, 34, 5, 9] => [333, 303030, 343434, 555, 999] 1000이하이므로 1 자리 수를 대비해 3번 반복
    return str(int(''.join(num)))