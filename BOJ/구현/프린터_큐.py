#1966번 실버3
case = int(input())
for _ in range(case):
    answer = 0
    n, m = map(int, input().split())
    doc_list = list(map(int, input().split()))
    doc_idx_list = []
    for idx in range(len(doc_list)):
        doc_idx_list.append((idx, doc_list[idx]))
    doc_list.sort()
    while True:
        idx, doc = doc_idx_list.pop(0)
        if doc == max(doc_list):
            doc_list.pop()
            answer += 1
            if idx == m:
                print(answer)
                break    
        else:
            doc_idx_list.append((idx, doc))