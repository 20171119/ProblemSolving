import sys
def solution(card, shuffle):
    parent = [c for c in range(len(card))]
    shufflenew =  [s - 1 for s in shuffle]
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

    for s in range(len(parent)):
        union(s, shufflenew[s])
    print(parent)
    for o in range(len(parent)):
        if card[o] != card[parent[o]]:
            answer += 1
    return answer

print(solution([1,1,2,2,1,1], [2,1,4,5,3,6]))
print(solution([1,2,3,4], [2,3,4,1]))