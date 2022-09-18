s = input()
result = int(s[0])

for i in range(len(s)-1):
    next_num = int(s[i+1])
    if result == 0 or result == 1 or next_num == 0 or next_num == 1:
        result += next_num
    else:
        result *= next_num

print(result)