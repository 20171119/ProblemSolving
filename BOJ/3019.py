# 실버1  테트리스
# 각 블록마다 회전하여 필드에 떨어트렸을때, 딱 맞게 떨어지는 필드의 높이를 숫자로 표현
# https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-3019%EB%B2%88-%ED%85%8C%ED%8A%B8%EB%A6%AC%EC%8A%A4-%EC%B4%88%EC%BD%94%EB%8D%94 참고

import sys

c, p = map(int, input().split())
maps = list(map(int, sys.stdin.readline().split()))
result = 0

if p == 1:
    result += c
    for i in range(c - 3):
        # 0000
        if (
            maps[i] == maps[i + 1]
            and maps[i + 1] == maps[i + 2]
            and maps[i + 2] == maps[i + 3]
        ):
            result += 1

if p == 2:
    for i in range(c - 1):
        # 00
        if maps[i] == maps[i + 1]:
            result += 1

if p == 3:
    for i in range(c - 2):
        # 001
        if maps[i] == maps[i + 1] and maps[i + 1] == maps[i + 2] - 1:
            result += 1
    for i in range(c - 1):
        # 10
        if maps[i] == maps[i + 1] + 1:
            result += 1

if p == 4:
    for i in range(c - 2):
        # 100
        if maps[i] == maps[i + 1] + 1 and maps[i + 1] == maps[i + 2]:
            result += 1
    for i in range(c - 1):
        # 01
        if maps[i] == maps[i + 1] - 1:
            result += 1

if p == 5:
    for i in range(c - 2):
        # 000
        if maps[i] == maps[i + 1] and maps[i + 1] == maps[i + 2]:
            result += 1
        # 101
        if maps[i] == maps[i + 1] + 1 and maps[i + 1] == maps[i + 2] - 1:
            result += 1
    for i in range(c - 1):
        # 10
        if maps[i] == maps[i + 1] - 1:
            result += 1
        # 10
        if maps[i] == maps[i + 1] + 1:
            result += 1

if p == 6:
    for i in range(c - 2):
        # 000
        if maps[i] == maps[i + 1] and maps[i + 1] == maps[i + 2]:
            result += 1
        # 011
        if maps[i] == maps[i + 1] - 1 and maps[i + 1] == maps[i + 2]:
            result += 1
    for i in range(c - 1):
        # 00
        if maps[i] == maps[i + 1]:
            result += 1
        # 20
        if maps[i] == maps[i + 1] + 2:
            result += 1

if p == 7:
    for i in range(c - 2):
        # 000
        if maps[i] == maps[i + 1] and maps[i + 1] == maps[i + 2]:
            result += 1
        # 110
        if maps[i] == maps[i + 1] and maps[i + 1] == maps[i + 2] + 1:
            result += 1
    for i in range(c - 1):
        # 02
        if maps[i] == maps[i + 1] - 2:
            result += 1
        # 00
        if maps[i] == maps[i + 1]:
            result += 1

print(result)
