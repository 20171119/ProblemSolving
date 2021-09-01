n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # x,y 가 그래프 밖이면 끝
    if x<0 or x>=n or y<0 or y>=m:
        return False

    # 해당 위치가 아직 방문 전이면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 동, 서, 남, 북 으로 dfs 실행
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    # 해당 위치가 얼음이면
    return False

result = 0
for x in range(n):
    for y in range(m):
        if dfs(x,y) == True:
            result += 1

print(result)
