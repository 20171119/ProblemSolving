# BOJ 9093 브론즈1
# [::-1] 로도 뒤집기 가능 or reverse 사용
import sys

case_num = int(sys.stdin.readline())


def reverse_sentence(sentence):
    stack = []
    for s in sentence:
        stack.append(s[::-1])
    return stack


for _ in range(case_num):
    sentence = sys.stdin.readline().split()
    result = reverse_sentence(sentence)
    print(" ".join(result))
