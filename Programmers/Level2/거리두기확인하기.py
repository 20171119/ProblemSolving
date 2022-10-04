from collections import deque

def solution(places):
    answer = []
    
    for place in places:
        graph, people = [], []
        for p in place:
            graph.append(list(p))
    
        for i in range(5):
            for j in range(5):
                if graph[i][j] == "P":
                    people.append((i,j))
        
        flag = True
        for x,y in people:
            if not check(x,y, graph):
                answer.append(0)
                flag = False
                break
        if flag:
            answer.append(1)
    
    return answer

def check(x, y, graph):
    q = deque()
    q.append((x, y, 0))
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    distance = 0
    
    while q:
        x, y, d = q.popleft()
        if d >= 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if graph[nx][ny] == "X":
                continue
            if graph[nx][ny] == "P":
                return False
            if graph[nx][ny] == "O":
                q.append((nx, ny, d+1))
                graph[x][y] = "X"
    return True