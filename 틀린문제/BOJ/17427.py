# 실버2 약수의 합2
# 제한시간 0.5초 -> 약수 하나씩 구하면 시간초과남
# https://y00n-lee.tistory.com/41?category=951814 참고
# (n // start) * start -> (n 이하에서 start를 약수로 갖는 숫자 개수) * 약수 start
n = int(input())
start = 1
result = 0
while n >= start:
    result += (n // start) * start
    start += 1

print(result)
