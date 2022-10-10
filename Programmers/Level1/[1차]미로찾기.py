def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin1 = bin(arr1[i])[2:]
        bin2 = bin(arr2[i])[2:]
        answer.append(add_binary(bin1, bin2, n))
    return answer

def add_binary(bin1, bin2, n):
    while len(bin1) < n:
        bin1 = "0" + bin1
    while len(bin2) < n:
        bin2 = "0" + bin2
    
    result = []
    for i in range(n):
        if bin1[i] == "0" and bin2[i] == "0":
            result.append(0)
        else:
            result.append(1)
    s = ""
    for i in result:
        if i == 1:
            s += "#"
        else:
            s += " "
    return s

# 다른사람 풀이 (비트연산 | 와 rjust 이용)
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer