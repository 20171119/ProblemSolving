n, m = map(int, input().split())
print(n,m)
card_array = []
result = 0
for _ in range(n):
  card_array.append(list(map(int, input().split())))
for card in card_array:
  min_card = min(card)
  result = max(min_card, result)

print(result)