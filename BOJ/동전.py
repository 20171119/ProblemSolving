# 11047번 실버2
answer = 0
n, k = map(int, input().split())
coin_list = []
for i in range(n):
    coin_list.append(int(input()))

for i in range(n-1, -1, -1): # 인덱스 거꾸로 => 큰 동전부터 비교
    if k == 0:
        break
    coin = coin_list[i]
    answer += k // coin
    k = k % coin

print(answer)