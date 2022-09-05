n = int(input())
arr = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

arr.sort()

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return False

for i in x:
    if binary_search(0, n-1, i):
        print("yes", end=" ")
    else:
        print("no", end=" ")