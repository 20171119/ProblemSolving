# 골드3 종이조각
# 비트마스크 - https://vixxcode.tistory.com/m/23 참고
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
papers = []
for _ in range(n):
    papers.append(list(map(int, input().rstrip())))
answer = 0

# 한칸당 가로, 세로 2가지 경우의 수가 있으므로 모든 칸의 경우의 수는 2^(n*m)
for i in range(1 << n*m):
    total = 0
    # 가로합
    for row in range(n):
        rowsum = 0
        for col in range(m):
            idx = row * m + col
            if i & (1 << idx) != 0: # 0 이면 세로, 아니면 가로
                rowsum = rowsum * 10 + papers[row][col]
            else:
                total += rowsum
                rowsum = 0
        total += rowsum
    
    # 세로합
    for col in range(m):
        colsum = 0
        for row in range(n):
            idx = row * m + col
            if i & (1 << idx) == 0:
                colsum = colsum * 10 + papers[row][col]
            else:
                total += colsum
                colsum = 0
        total += colsum
    answer = max(answer, total)

print(answer)
