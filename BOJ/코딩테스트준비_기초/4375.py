# 실버3 1
while True:
    try:
        n = int(input())
    except EOFError:  # 입력이 끝날대 까지 받으려면?? -> EOF 이용
        break

    if n == 1:
        print("1")
        continue

    num, result = 1, 1
    while True:
        result += 1
        num = num * 10 + 1  # 1, 11, 111, 1111 ....
        if num % n == 0:
            print(result)
            break
