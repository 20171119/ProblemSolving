# 실버1 하노이 탑 이동 순서
def solve(n, start, end):
    if n == 1:
        print(start, end)
        return
    else:
        solve(n-1, start, 6-start-end) # 1단계 -> n-1개를 1번에서 2번으로 옮기기
        print(start, end) # 2단계 -> 가장 아래 1개를 1번에서 3번 옮기기
        solve(n-1, 6-start-end, end) # 3단계 -> n-1개를 2번에서 3번 옮기기

n = int(input())
print(2**n-1)
solve(n, 1, 3)