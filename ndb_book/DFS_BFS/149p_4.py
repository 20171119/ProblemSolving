n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 얼음 틀을 벗어난다면
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 칸막이라면
    if graph[x][y] == 1:
        return False

    # 방문했다고 표시
    graph[x][y] = 1
    
    # (x,y) 얼음틀에서 상,하,좌,우 확인
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True


result = 0
# 얼음 틀의 좌표를 하나씩 확인하면서 dfs 처리 하면 아이스크림 개수 나옴
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)