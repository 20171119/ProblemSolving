def solution(numbers, hand):
    answer = ''
    key2idx = {"1":(0,0), "2":(0,1), "3":(0,2), 
               "4":(1,0), "5":(1,1), "6":(1,2),
               "7":(2,0), "8":(2,1), "9":(2,2),
               "*":(3,0), "0":(3,1), "#":(3,2)}
    left, right = "*", "#"

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left = number
        if number in [3, 6, 9]:
            answer += "R"
            right = number
        if number in [2,5,8,0]:
            x, y = key2idx[str(number)]
            left_x, left_y = key2idx[str(left)]
            right_x, right_y = key2idx[str(right)]
            left_d = abs(x-left_x) + abs(y-left_y)
            right_d = abs(x-right_x) + abs(y-right_y)
            if left_d > right_d:
                answer += "R"
                right = number
            elif left_d < right_d:
                answer += "L"
                left = number
            else:
                if hand == "left":
                    answer += "L"
                    left = number
                else:
                    answer += "R"
                    right = number
    return answer