# 벽 3개를 맵에 세울수 있는 모든 경우의수를 반복하여 안전영역이 가장 크게 되는 결과를 얻는다.
from itertools import combinations
from collections import deque
import copy

# 바이러스 퍼지는 함수 구현
def virus(graph, virus_list):
    blank = 0 # 빈칸 개수
    queue = deque()
    # 4방향
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 모든 바이러스의 x,y 좌표를 queue에 넣음
    for v in virus_list:
        x, y = v
        queue.append((x,y))
        
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 밖을 벗어난다면 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 벽이라면 무시
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx,ny))   
    # 총 빈칸 개수
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                blank += 1
    return blank

def solution():
    # 벽을 세울 수있는 모든 x,y 좌표를 구함 / 바이러스가 있는 x,y 좌표 구함
    wall_list = []
    virus_list = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                wall_list.append((i,j))
            elif graph[i][j] == 2:
                virus_list.append((i,j))
    answer = 0
    for walls in list(combinations(wall_list, 3)):
        # deep copy -> 서로 영향 주지 않음 // 벽 3개를 임의로 세운후 바이러스 확산 테스트 하기 위한 deep copy
        test_graph = copy.deepcopy(graph)
        for wall in walls:
            x, y = wall
            test_graph[x][y] = 1
        num = virus(test_graph, virus_list)
        answer = max(answer, num)
    return answer

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(solution())