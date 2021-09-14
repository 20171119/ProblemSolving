n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
# 어차피 n 은 2 이상이고, 가장 큰수를 만드려면 첫번째껄 반복하다가 k번 초과하면 두번째걸 한번씩만 더해주면 됨.
first = numbers[0]
second = numbers[1]
answer = 0

count = 1
check = 1

while count <= m:
    if check > k:
        check = 1
        answer += second
        count += 1
    else:
        answer += first
        count += 1
        check += 1
print(answer)
