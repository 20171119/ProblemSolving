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
def solution(k, dungeons):
    global answer, visited
    answer = 0
    visited = [0] * len(dungeons)
    def dfs(k, result):
        global answer, visited
        if result > answer:
            answer = result
        
        for i in range(len(visited)):
            if k >= dungeons[i][0] and not visited[i]:
                visited[i] = 1
                dfs(k - dungeons[i][1], result + 1)
                visited[i] = 0
        
    dfs(k, 0)
    return answer