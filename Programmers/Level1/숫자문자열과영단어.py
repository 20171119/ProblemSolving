def solution(s):
    str_num = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    int_num = [str(i) for i in range(0, 10)]
    answer = ""
    temp = ""
    for i in range(len(s)):
        temp += s[i]
        if temp in int_num:
            answer += temp
            temp = ""

        elif temp in str_num:
            idx = str_num.index(temp)
            answer += int_num[idx]
            temp = ""
    return int(answer)
