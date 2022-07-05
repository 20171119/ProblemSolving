n = int(input())
items = list(map(int, input().split()))
m = int(input())
requests =list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return False

items.sort()

for request in requests:
    if binary_search(items, request, 0, len(items)-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')