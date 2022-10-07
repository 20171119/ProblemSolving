def solution(arr):
    answer = [0, 0]
    
    def compression(row, col, length):
        start = arr[row][col]
        for i in range(row, row + length):
            for j in range(col, col + length):
                if arr[i][j] != start:
                    length = length // 2
                    compression(row, col, length)
                    compression(row, col + length, length)
                    compression(row + length, col, length)
                    compression(row + length, col + length, length)
                    return
                    
        answer[start] += 1
        
    
    compression(0, 0, len(arr))
    
    return answer