# 실버3 다음 순열
# next_permutation 알고리즘 이용하기
# ex) 1432 -> 2134
# 1. 뒤에서 부터 순열을 비교하며, 뒷 값이 앞 값보다 큰 경우까지 반복 -> x인덱스 1 y인덱스 4
# 2. 다시 뒤에서 부터 값을 비교하며 x 인덱스보다 큰값이 있으면 swap -> 1과 2 스왑
# 3. y 인덱스 부터 오름차순 정렬 2 + 134 => 2134
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
