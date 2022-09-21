n = input()
mid = len(n) // 2
left_n = n[:mid]
right_n = n[mid:]

sum_left, sum_right = 0, 0
for i in left_n:
    sum_left += int(i)
for i in right_n:
    sum_right += int(i)

if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")