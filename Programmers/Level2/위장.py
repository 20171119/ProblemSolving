# 해시
def solution(clothes):
    answer = 1
    BIC_DIC = {item[1] : 1 for item in clothes}
    #    temp[clothes[i][1]] = 1#아무것도 안입은 상태를 하나 가지고 있다고보고 생성
    for item in clothes:
        BIC_DIC[item[1]] += 1
        #각 파츠별 개수 더해주기
    for k in BIC_DIC.values():#경우의 수 구하기
        answer = answer * k

    return answer - 1