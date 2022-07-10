import heapq
from re import L
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int ,input().split()) # 노드 개수, 간선 개수
start = int(input()) # 시작 번호
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a 노드에서 b 노드로 가는 비용이 c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start)) # (거리, 노드번호)
    distance[start] = 0
    while q:
        # 최단거리의 노드에 대한 정보
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧을 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    # 도달할수 없는 경우 INF 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
