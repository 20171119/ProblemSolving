# 실버2 랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lengths = []
for _ in range(k):
    lengths.append(int(input()))

def get_count(mid):
    count = 0
    for l in lengths:
        count += l // mid
    return count

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        print(start, end, mid)
        result = get_count(mid)
        if result >= n: # 자른 개수가 더 많으면 -> 크게 잘라야함
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(1, max(lengths)))