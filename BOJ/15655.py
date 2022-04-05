# 실버3 N과 M (6)
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []


def dfs(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(start, N):
        if not nums[i] in result:
            result.append(nums[i])
            dfs(i + 1)
            result.pop()


dfs(0)
