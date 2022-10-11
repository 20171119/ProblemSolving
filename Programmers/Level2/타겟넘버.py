def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(start, temp): # 시작 인덱스, 중간 합계
        global answer
        
        if start >= len(numbers):
            if temp == target:
                answer += 1
            return
        
        dfs(start + 1, temp + numbers[start])
        dfs(start + 1, temp - numbers[start])
    
    dfs(0, 0)
    
    return answer

# 다른사람 풀

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])