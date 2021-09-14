n, m = map(int, input().split())
answer = 0
for _ in range(n):
    cards = list(map(int, input().split()))
    answer = max(answer, min(cards))
print(answer)
