# 골드5 수 묶기
# 음수, 0, 1, 2이상 양수
# 음수가 2개 이상일때는 오름차순일 때 앞에서부터 서로 곱하다가 마지막 음수는 0이랑 곱하기
# 1은 그냥 더하기
# 2이상 양수는 오름차순일 때 뒤에서부터 곱하다가 마지막 수는 더하기
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

answer = 0
minus, plus = [], []
zero = False
for i in range(n):
    if arr[i] < 0:
        minus.append(arr[i])
    elif arr[i] == 0:
        zero = True
    elif arr[i] == 1:
        answer += 1
    else:
        plus.append(arr[i])

while len(minus) >= 2:
    n1 = minus.pop(0)
    n2 = minus.pop(0)
    answer += n1 * n2

if not zero and minus:
    answer += minus[0]

while len(plus) >= 2:
    n1 = plus.pop()
    n2 = plus.pop()
    answer += n1 * n2

print(answer + sum(plus))