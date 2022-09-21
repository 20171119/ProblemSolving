from curses.ascii import isalnum


s = list(map(str, input()))
num_list = [str(i) for i in range(10)]
chars = []
numbers = []
for i in s:
    if i in num_list:
        numbers.append(int(i))
    else:
        chars.append(i)

chars.sort()
result = "".join(chars)
if sum(numbers) != 0:
    result += str(sum(numbers))
print(result)
