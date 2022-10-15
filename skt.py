import sys
def solution(card, shuffle):
    parent = [c for c in range(len(card))] # 원래 인덱스
    shufflenew =  [s - 1 for s in shuffle] # 바뀐 인덱스
    answer = 0

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        x = find(x)
        y = find(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    for s in range(len(parent)): # 원래 인덱스와 바뀐 인덱스를 합치기
        union(s, shufflenew[s])
    print(parent)
    for o in range(len(parent)):
        if card[o] != card[parent[o]]: # 합친 인덱스가 원래 인덱스와 다르다면 변경 필요한 것
            answer += 1
    return answer

print(solution([1,1,2,2,1,1], [2,1,4,5,3,6]))
print(solution([1,2,3,4], [2,3,4,1]))