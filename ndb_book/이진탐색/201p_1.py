n, m = map(int, input().split())
heights = list(map(int, input().split()))

def get_sum(mid):
    result = 0
    for h in heights:
        temp = h - mid
        if temp > 0:
            result += temp
    return result

def binary_search(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        result = get_sum(mid)
        if result == m:
            answer = mid
            break
        elif result > m:
            answer = mid
            start = mid + 1
        else:
            end = mid -1
    return answer

print(binary_search(0, max(heights)))
    