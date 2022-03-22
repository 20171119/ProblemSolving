# 달팽이는 올라가고 싶다 브론즈1
# 반복문으로 하면 시간초과 남!!
# A + (A-B) * result >= V
# result >= (V-A)/(A-B)
a, b, v = map(int, input().split())
if (v-a)%(a-b) == 0:
    print(int((v-a)/(a-b)) + 1)
else:
    print(int((v-a)/(a-b)) + 2)
