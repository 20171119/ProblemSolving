def solution(want, number, discount):
    answer = 0
    wants = []
    for i in range(len(number)):
        for _ in range(number[i]):
            wants.append(want[i])
    wants.sort()
    
    for i in range(len(discount) - 9):
        sales = discount[i:i+10]
        sales.sort()
        if sales == wants:
            answer += 1
        
            
    return answer