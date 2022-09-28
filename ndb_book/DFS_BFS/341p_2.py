# 벽 3개 세우기 (조합 이용) -> 바이러스 퍼지기 -> 남은 면적 구하기 
from itertools import combinations
import copy
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
temp = copy.deepcopy(graph)

wall_list = []
virus_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall_list.append((i,j))
        if graph[i][j] == 2:
            virus_list.append((i,j))

def virus(graph, virus_list):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque()
    for virus in virus_list:
        q.append(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx,ny))
    return graph
    

def get_result(graph):
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                answer += 1
    return answer


result = 0
for walls in list(combinations(wall_list, 3)):
    temp = copy.deepcopy(graph)
    for x,y in walls:
        temp[x][y] = 1
    temp = virus(temp, virus_list)
    result = max(result, get_result(temp))
print(result)