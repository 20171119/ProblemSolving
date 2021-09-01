n = int(input())
plans = list(input().split())

x,y = 0,0
for plan in plans:
  if plan == 'U':
    if x-1 > 0:
      x = x-1
  if plan == 'D':
    if x+1 <n:
      x = x+1
  if plan == 'L':
    if y-1 > 0:
      y = y-1
  if plan == 'R':
    if y+1 < n:
      y = y+1


print(x+1, y+1)
