def solution(numbers):
    answer = []
    for number in numbers:
        binary = list('0' + format(number, 'b'))
        idx = ''.join(binary).rfind('0')
        binary[idx] = '1'
        if number % 2 != 0:
            binary[idx + 1] = '0'
        answer.append(int(''.join(binary), 2))
    return answer