# 실버1 물병
n, k = map(int, input().split())

answer = 0
while bin(n).count("1") > k:
    answer += 1
    n += 1
print(answer)