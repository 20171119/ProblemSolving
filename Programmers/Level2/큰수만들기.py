def solution(number, k): 
    answer = [] # stack 처럼 활용
    for n in number:
        if not answer: # stack 비어있을 때
            answer.append(n)
            continue
        if k > 0:
            while answer[-1] < n: # 가장 위의 값이 n 보다 작다면
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(n)
    
    if k > 0: # ex) 9421 일시 k = 2
        answer = answer[:-k]
    return ''.join(answer)

# 조합으로 풀시 시간 초과
# import itertools
# def solution(number, k):
#     answer = ''
#     number_list = list(number)
#     nCr = list(map(''.join, itertools.combinations(number_list, len(number) - k)))
#     nCr.sort(reverse=True)
#     print(nCr)
#     return nCr[0]