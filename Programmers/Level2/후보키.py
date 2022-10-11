from itertools import combinations

def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])
    
    combi = [] # 컬럼의 가능한 조합 리스트
    for i in range(1, col + 1):
        for com in list(combinations(range(col), i)):
            combi.append(com)
    
    unique = []
    for com in combi:
        temp = [tuple([r[i] for i in com]) for r in relation]
        flag = True
        if len(set(temp)) == row: # 유일성 검사
            for u in unique:
                if set(u).issubset(com): # 최소성 검사
                    flag = False
                    break
            if flag:
                unique.append(com)
                
    return len(unique)