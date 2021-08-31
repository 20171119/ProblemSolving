#스택/큐
# pop 으로 풀었을때 시간초과 났었음.
def solution(prices):
    answer = []
    for j in range(len(prices)):
        for i in range(j+1,len(prices)):
            if prices[j] > prices[i]:
                break
        answer.append(i-j)
    return answer



# def solution(prices):
#     answer = []
#     while prices:
#         out = prices.pop(0)
#         time = 0
#         for i in range(len(prices)):
#             time += 1
#             if out > prices[i]:
#                 break
#         answer.append(time)
#     return answer