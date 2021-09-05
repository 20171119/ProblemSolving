def solution(answers):
    answer = []
    m1 = [1,2,3,4,5] #1번 - 12345
    m2 = [2,1,2,3,2,4,2,5] #2번 - 21232425
    m3 = [3,3,1,1,2,2,4,4,5,5] #3번 - 3311224455
    
    c1, c2, c3 = 0, 0, 0 # 수포자 1,2,3이 각각 맞춘 문제 수
    for i in range(len(answers)):
        i1 = i % len(m1)
        i2 = i % len(m2)
        i3 = i % len(m3)
        if answers[i] == m1[i1]:
            c1 += 1
        if answers[i] == m2[i2]:
            c2 += 1 
        if answers[i] == m3[i3]:
            c3 += 1
    
    if c1 == max(c1,c2,c3):
        answer.append(1)
    if c2 == max(c1,c2,c3):
        answer.append(2)
    if c3 == max(c1,c2,c3):
        answer.append(3)
    return answer