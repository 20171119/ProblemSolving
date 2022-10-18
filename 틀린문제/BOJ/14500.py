# 테트로미노 골드5 - 10/18
import sys
input = sys.stdin.readline

# ㅗ 모양 빼고 점수 구하기
def get_score(row, col, total, count):
    global answer
    if answer >= total + max_val * (4 - count): # 최대값 백트랙킹 -> 종이의 최대값을 남은 개수에 더한것보다 크다면 종료시키기
        return

    if count == 4:
        answer = max(answer, total)
        return
    
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            get_score(nx, ny, total + paper[nx][ny], count + 1)
            visited[nx][ny] = False
    
# ㅗ 모양에서 점수 구하기
def get_rest_score(row, col):
    global answer
    for i in range(4):
        score = paper[row][col]
        for j in range(3):
            idx = (i+j) % 4 # dx dy 인덱스의 012 123 230 301
            nx = row + dx[idx]
            ny = col + dy[idx]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                score = 0
                break
            score += paper[nx][ny]
        answer = max(answer, score)


N, M = map(int, input().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_val = max(map(max, paper))
answer = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        get_score(i, j, paper[i][j], 1)
        visited[i][j] = False
        get_rest_score(i, j)

print(answer)