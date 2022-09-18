s = input()
group_0 = 0
group_1 = 0

for i in range(len(s)):
    now = int(s[i])
    if i == len(s) -1:
        if now == 0:
            group_0 += 1
        else:
            group_1 += 1
        break

    next = int(s[i+1])
    if now == next:
        continue
    if now == 0:
        group_0 += 1
    else:
        group_1 += 1
    
if group_0 < group_1:
    print(group_0)
else:
    print(group_1)