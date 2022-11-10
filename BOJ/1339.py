# 골드4 단어 수학
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
# words.sort(key=lambda x: -len(x))

dic = defaultdict(int) # 알파벳: 우선순위 점수

for word in words:
    for i in range(len(word)):
        dic[word[i]] += 10**(len(word)-1-i)

dic = dict(sorted(dic.items(), key=lambda item: -item[1])) # 점수 순으로 내림차순 정렬

num = 9
answer = 0
for v in dic.values(): # 높은 점수 부터 9~1 까지 부여하면서 더하면 정답
    answer += num * v
    num -= 1

print(answer)