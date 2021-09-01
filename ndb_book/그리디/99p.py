n, k = map(int, input().split())
count = 0
while n != 1:
  while n%k == 0:
    if n == 1 :
      break
    n = n//k
    count += 1
  if n == 1:
    break
  n = n - 1
  count += 1
print(count)