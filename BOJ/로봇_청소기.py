#14503번 골드5
n, m = map(int, input().split())
r, c, d = map(int, input().split())
locs = []
check_locs = []
for _ in range(n):
    ls = list(map(int, input().split()))
    locs.append(ls)
    check_locs.append(ls)

# 0 - 북, 1- 동, 2- 남, 3 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
flag = True

# 빈칸 0, 벽 1, 청소 2
while flag:
    if locs[r][c] == 0:
        locs[r][c] = 2
        answer += 1
    for i in range(1,5):
        d_check = (d-i)
        if d_check < 0:
            d_check += 4
            d_check = d_check % 4
        x = r + dx[d_check]
        y = c + dy[d_check]
    
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if locs[x][y] == 0:
            r, c= x, y
            d = d_check
            break
        if i == 4:
            check_x = r-dx[d_check]
            check_y = c-dy[d_check]
            if locs[check_x][check_y] == 2:
                r, c= check_x, check_y
                break
            else:
                flag = False
                break
print(answer)

    

