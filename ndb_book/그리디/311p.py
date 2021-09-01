n = int(input())
users = list(map(int, input().split()))
users.sort()
result = 0
num = 0
for index in range(n):
  fear = users[index]
  num += 1
  if fear <= num:
    result += 1
    num = 0 

print(result)
  