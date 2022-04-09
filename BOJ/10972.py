# 실버3 다음 순열
# next_permutation 알고리즘 이용하기
# dfs 로 풀려하니 런타임 에러뜸...
N = int(input())
current = list(map(int, input().split()))
check = 0
reverse = True

for i in range(N - 1, 0, -1):
    if current[i - 1] < current[i]:
        check = i - 1
        reverse = False
        break

if reverse:
    print("-1")
else:
    for i in range(N - 1, 0, -1):
        if current[check] < current[i]:
            current[check], current[i] = current[i], current[check]
            result = current[: check + 1] + sorted(current[check + 1 :])
            print(" ".join(map(str, result)))
            break
