# 실버 3 N과 M (2)
N, M = map(int, input().split())
visited = [False] * N
result = []


def solution(N, M, start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            result.append(i + 1)
            solution(N, M, i + 1)
            result.pop()
            visited[i] = False


solution(N, M, 0)
