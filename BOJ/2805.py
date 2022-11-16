# 실버2 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

def get_height(h):
    result = 0
    for height in heights:
        if height > h:
            result += height - h
    return result

def binary_search(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        h = get_height(mid)
        if h == m:
            answer = mid
            break
        elif h > m:
            start = mid + 1
            answer = mid
        elif h < m:
            end = mid - 1
    return answer

print(binary_search(0, max(heights)))