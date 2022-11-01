# 골드4 카드 정렬하기
# heapq 이용한 문제
import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    answer = 0
    while len(cards) > 1:
        min1 = heapq.heappop(cards)
        min2 = heapq.heappop(cards)
        answer += min1 + min2
        heapq.heappush(cards, min1 + min2)
    print(answer)