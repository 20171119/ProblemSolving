def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] != 0:
                stack.append(board[row][move-1])
                board[row][move-1] = 0
                
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                break
    return answer