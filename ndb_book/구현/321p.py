n =  input()
length = len(n)//2
first = n[:length]
second = n[length:]

first_sum = 0
for i in first:
  first_sum += int(i)

second_sum = 0
for i in second:
  second_sum += int(i)

if first_sum == second_sum:
  print("LUCKY")
else:
  print("READY")