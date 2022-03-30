# 사탕게임 실버3
# python3 로 하면 시간초과, pypy3 로 하니까 됨..
def get_result(boards):
    result = 0
    # 가로 체크
    for x in range(n):
        temp = 1
        for y in range(n):
            if y >= n - 1:
                break
            if boards[x][y] == boards[x][y + 1]:
                temp += 1
                result = max(result, temp)
            else:
                temp = 1
    # 세로 체크
    for y in range(n):
        temp = 1
        for x in range(n):
            if x >= n - 1:
                break
            if boards[x][y] == boards[x + 1][y]:
                temp += 1
                result = max(result, temp)
            else:
                temp = 1
    return result


n = int(input())
boards = []
for _ in range(n):
    boards.append(list(input()))

result = 0
# 가로 바꾸기
for x in range(n):
    for y in range(n):
        if y >= n - 1:
            break
        boards[x][y], boards[x][y + 1] = boards[x][y + 1], boards[x][y]
        result = max(result, get_result(boards))
        boards[x][y], boards[x][y + 1] = boards[x][y + 1], boards[x][y]

# 세로 바꾸기
for y in range(n):
    for x in range(n):
        if x >= n - 1:
            break
        boards[x][y], boards[x + 1][y] = boards[x + 1][y], boards[x][y]
        result = max(result, get_result(boards))
        boards[x][y], boards[x + 1][y] = boards[x + 1][y], boards[x][y]

print(result)
