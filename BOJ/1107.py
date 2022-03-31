# 리모컨 골드5
def check_btn(n):
    num = list(str(n))
    for i in num:
        if i in btns:
            return False
    return True


N = int(input())
M = int(input())
if M == 0:
    btns = []
else:
    btns = list(input().split())

result = abs(N - 100)
for i in range(1000001):
    if check_btn(i):
        result = min(result, len(str(i)) + abs(i - N))
print(result)
