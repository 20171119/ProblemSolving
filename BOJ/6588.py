# 실버1 골드바흐의 추축
import sys

MAX = 1000001
arr = [True for _ in range(MAX)]
for i in range(2, MAX):
    if arr[i]:
        for k in range(i + i, MAX, i):
            arr[k] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    flag = True

    for a in range(3, n):
        if arr[a] and arr[n - a]:
            print(str(n) + " = " + str(a) + " + " + str(n - a))
            flag = False
            break
    if flag:
        print("Goldbach's conjecture is wrong.")
