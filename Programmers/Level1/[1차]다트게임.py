def solution(dartResult):
    answer = 0
    
    num = ''
    score = []
    for dart in dartResult:
        if dart.isnumeric():
            num += dart
        else:
            if dart in ["S", "D", "T"]:
                num = int(num)
                if dart == "S":
                    score.append(num**1)
                if dart == "D":
                    score.append(num**2)
                if dart == "T":
                    score.append(num**3)
                num = ''
            else:
                if dart == "*":
                    if len(score) >= 2:
                        score[-2] = score[-2] * 2
                    score[-1] = score[-1] * 2
                if dart == "#":
                    score[-1] = score[-1] * (-1)
        
    return sum(score)