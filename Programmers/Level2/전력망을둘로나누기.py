from collections import deque
import copy

def solution(n, wires):
    answer = n
    for i in range(len(wires)): # n-1개의 wires들을 하나씩 제거하는 모든 경우의 수
        temp = copy.deepcopy(wires)
        del temp[i]
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        
        for wire in temp:
            a, b = wire
            graph[a].append(b)
            graph[b].append(a)
            
        count = get_count(graph, 1, visited)
        rest = n - count
        answer = min(answer, abs(rest-count))
    return answer

def get_count(graph, start, visited):
    count = 1
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1
    return count