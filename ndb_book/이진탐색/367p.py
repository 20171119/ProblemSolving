from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

left = bisect_left(arr, x)
right = bisect_right(arr, x)

if left == right:
    print(-1)
else:
    print(right-left)