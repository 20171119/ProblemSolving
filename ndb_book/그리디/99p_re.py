n, k = map(int, input().split())
count = 0
# 최대한 많이 k로 나누기 (1로 뺴는 것보다 n을 작게 만들수 있어서)
while n > 1:
    if n % k == 0:
        n = n // k
        count += 1
    else:
        n = n - 1
        count += 1
print(count)