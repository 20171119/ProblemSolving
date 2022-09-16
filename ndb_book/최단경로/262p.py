import heapq
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        # 최단거리가 가장 짧은 노드 선택
        dist, now = heapq.heappop(q)
        # 최소 거리인지 확인 (방문했는지 확인)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드를 거치는 게 더 짤을 때
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

num = 0
time = 0
for d in distance:
    if d == INF:
        continue
    num += 1
    time = max(time, d)
print(num-1, time)