n = int(input())
count = 0
coin_list = [500, 100, 50 ,10]
for coin in coin_list:
    count += n//coin
    n = n%coin
print(count)