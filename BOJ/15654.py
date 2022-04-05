# 실버3 N과 M (5)
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []


def dfs():
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in nums:
        if not i in result:
            result.append(i)
            dfs()
            result.pop()


dfs()
