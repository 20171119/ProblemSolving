# 실버 3 N과 M(1)
N, M = map(int, input().split())
visitied = [False] * N
result = []


def get_result(N, M):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(N):
        if not visitied[i]:
            visitied[i] = True
            result.append(i + 1)
            get_result(N, M)
            result.pop()
            visitied[i] = False


get_result(N, M)
