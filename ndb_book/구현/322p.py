s = input()
ord_strlist = []
ord_numlist = []
for i in s:
  if ord(i) < 65:
    ord_numlist.append(i)
  else:
    ord_strlist.append(i)

ord_strlist.sort()
num = 0
for i in ord_numlist:
  num += int(i)
ord_strlist.append(str(num))
answer = ''.join(ord_strlist)
print(answer)