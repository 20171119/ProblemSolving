# 실버3 N과 M(8)
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []


def dfs(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(start, N):
        result.append(nums[i])
        dfs(i)
        result.pop()


dfs(0)
