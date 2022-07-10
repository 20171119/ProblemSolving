INF = int(1e9)

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 거리 정보 리스트, 모든값 무한 초기화
# 자기 자신 거리정보 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선 정보 받아 설정
for _ in range(m):
    a, b, c = map(int, input().split()) # a에서 b로 가는 비용 c
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 실행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할수 없는 경우 INF 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()