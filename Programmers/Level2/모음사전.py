from itertools import product

def solution(word):
    answer = 0
    aeiou = ["A", "E", "I", "O", "U"]
    strings = []
    for i in range(1, 6):
        for s in list(product(aeiou, repeat=i)):
            s = "".join(s)
            strings.append(s)
    strings.sort()
    answer = strings.index(word)
    return answer + 1