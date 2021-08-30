# 해시
def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        cmp_len = len(phone_book[i-1])
        if phone_book[i-1][0:cmp_len] == phone_book[i][0:cmp_len]:
            return False
    return True