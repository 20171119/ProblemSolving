# BOJ 9012 실버4
import sys

case_num = int(sys.stdin.readline())


def check_vps(ps):
    check = 0
    for i in ps:
        if i == "(":
            check += 1
        elif i == ")":
            check -= 1
        if check < 0:
            return False
    if check == 0:
        return True
    else:
        return False


for _ in range(case_num):
    ps = sys.stdin.readline().strip()
    result = check_vps(ps)
    if result:
        print("YES")
    else:
        print("NO")
