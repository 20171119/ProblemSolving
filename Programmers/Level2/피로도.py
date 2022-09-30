from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for combs in list(permutations(dungeons,len(dungeons))):
        temp = k
        result = 0
        for first, second in combs:
            if temp >= first:
                temp -= second
                result += 1
        answer = max(answer, result)
    return answer

# 백트랙킹
answer = 0
n = 0
visited = []
def dfs(k, result, dungeons):
    global answer
    if result > answer:
        answer = result
        
    for i in range(n):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k - dungeons[i][1], result + 1, dungeons)
            visited[i] = 0
    
def solution(k, dungeons):
    global n, visited, answer
    n = len(dungeons)
    visited = [0] * n
    dfs(k, 0, dungeons)
    return answer