from collections import defaultdict

def solution(skill, skill_trees):
    answer = 0
    dic = defaultdict(int) # 스킬네임: 번호
    for i in range(len(skill)):
        dic[skill[i]] = i
    for skill_tree in skill_trees:
        temp = []
        flag = True
        for s in skill_tree:
            if s in skill:
                if not temp and dic[s] == 0: # 맨처음 스킬이라면
                    temp.append(dic[s])
                elif dic[s] - 1 in temp: # 이전 스킬이 잇다면
                    temp.append(dic[s])
                else:
                    flag = False
                    break
        if flag:
            answer += 1
     
    return answer

# 다른사람 풀이
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer