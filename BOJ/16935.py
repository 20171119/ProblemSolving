# 실버1 배열 돌리기 3
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def cal1():
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[n-i-1][j]
    return temp

def cal2():
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][m-j-1]
    return temp

def cal3():
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = graph[n-1-j][i]
    return temp

def cal4():
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = graph[j][m-1-i]
    return temp

def cal5():
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):    # 1 -> 2
        for j in range(m // 2):
            temp[i][j + m // 2] = graph[i][j]
 
    for i in range(n // 2):    # 2 -> 3
        for j in range(m // 2, m):
            temp[i + n // 2][j] = graph[i][j]
 
    for i in range(n // 2, n):    # 3 -> 4
        for j in range(m // 2, m):
            temp[i][j - m // 2] = graph[i][j]
 
    for i in range(n // 2, n):    # 4 -> 1
        for j in range(m // 2):
            temp[i - n // 2][j] = graph[i][j]
 
    return temp

def cal6():
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):    # 1 -> 4
        for j in range(m // 2):
            temp[i + n // 2][j] = graph[i][j]
 
    for i in range(n // 2, n):    # 4 -> 3
        for j in range(m // 2):
            temp[i][j + m // 2] = graph[i][j]
 
    for i in range(n // 2, n):    # 3 -> 2
        for j in range(m // 2, m):
            temp[i - n // 2][j] = graph[i][j]
 
    for i in range(n // 2):    # 2 -> 1
        for j in range(m // 2, m):
            temp[i][j - m // 2] = graph[i][j]
 
    return temp

op = list(map(int, input().split()))
for o in op:
    if o == 1:
        graph = cal1()
    elif o == 2:
        graph = cal2()
    elif o == 3:
        graph = cal3()
        n, m = m, n
    elif o == 4:
        graph = cal4()
        n, m = m, n
    elif o == 5:
        graph = cal5()
    elif o == 6:
        graph = cal6()
for a in graph:
    print(*a)