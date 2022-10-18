#회의실 배정 실버2
#틀림 - 시간초과
n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

# sort 를 두번 이용해서 for 문 한번에 답을 찾도록 해야됨.
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])
last = 0
cnt = 0
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)

## 시간 초과 코드 - 이중 for 문

# n = int(input())
# meeting_list = []

# for _ in range(n):
#     start, end = map(int, input().split())
#     meeting_list.append((start, end))

# meeting_list.sort(key=lambda x: x[0])

# print(meeting_list)
# answer = 0
# for i in range(len(meeting_list)):
#     start1, end1 = meeting_list[i]
#     count = 1
#     for j in range(i+1, len(meeting_list)):
#         start2, end2 = meeting_list[j]
#         if end1 <= start2:
#             start1, end1 = start2, end2
#             count += 1
#     answer = max(answer, count)
# print(answer)