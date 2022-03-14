# 수 정렬하기2 실버4
# 기존 수 정렬하기 문제랑 똑같다고 생각했는데 시간초과남...
# 최대 입력이 1000000 이라 python 에서 제공하는 sort는 O(nlgn) 이므로 해결 가능
# 시간초과난 부분은 input 쪽을 sys로 안받아서 났음... (입력이 백만 넘어가면 sys로 받자!!)
import sys

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
for n in numbers:
    print(n)
