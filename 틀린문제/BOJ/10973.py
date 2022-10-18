# 실버3 이전 순열
# 1. 뒤에서부터 2개씩 비교해서 arr[i-1] > arr[i] 인 idx 찾음
# 2. idx 기준으로 나누어서 뒤에 배열중 arr[idx-1] > arr[j] 인  j를 찾음
# 3. arr[idx-1], arr[j]를 swap후 뒤에를 내림차순을 정렬
import sys

input = sys.stdin.readline

n = int(input())
current = list(map(int, input().split()))

idx = 0
for i in range(n - 1, 0, -1):
    if current[i - 1] > current[i]:
        idx = i
        break

if idx == 0:
    print("-1")
else:
    for i in range(n - 1, idx - 1, -1):
        if current[i] < current[idx - 1]:
            current[i], current[idx - 1] = current[idx - 1], current[i]
            result = current[:idx] + sorted(current[idx:], reverse=True)
            print(" ".join(map(str, result)))
            break
