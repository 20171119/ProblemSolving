money = int(input())
coins = [500, 100, 50, 10]
count = 0
for coin in coins:
    if money == 0:
        break
    count += money // coin
    money %= coin

print(count)