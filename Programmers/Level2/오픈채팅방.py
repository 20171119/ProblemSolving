def solution(record):
    answer = []
    dict = {}
    
    for r in record:
        r_split = r.split()
        if len(r_split) == 3: # Enter, Change
            dict[r_split[1]] = r_split[2]
        
    for r in record:
        r_split = r.split()
        if r_split[0] == "Enter":
            answer.append(dict[r_split[1]]+"님이 들어왔습니다.")
        elif r_split[0] == "Leave":
            answer.append(dict[r_split[1]]+"님이 나갔습니다.")
                    
    return answer