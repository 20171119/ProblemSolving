# 11399번 실버3
num = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
prev = 0
answer = 0
for n in num_list:
    after = n + prev
    prev = after
    answer += prev

print(answer)