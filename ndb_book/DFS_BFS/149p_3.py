n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input())))

answer = 0
def dfs(x, y):

    # 좌표를 벗어난다면
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 이미 얼음이라면
    if ice[x][y] == 1:
        return False

    ice[x][y] = 1 # 방문 처리
    # 상하좌우 처리
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True


for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(answer)