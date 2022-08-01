def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        array = []
        for s in skill_tree:
            if s in skill:
                array.append(s)
        
        flag = True
        for idx, val in enumerate(array):
            if val != skill[idx]:
                flag = False
                break
        if flag:
            answer += 1
        
    return answer