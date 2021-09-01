#실버2
first_list = input().split('-')
number_list = []
for first in first_list:
    if first.find('+') != -1:
        second_list = list(map(int, first.split('+')))
        add = sum(second_list)
        number_list.append(add)
    else:
        number_list.append(int(first))

answer = number_list.pop(0)
for number in number_list:
    answer -= number
print(answer)