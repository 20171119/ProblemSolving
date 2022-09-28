def solution(id_list, report, k):
    answer = []
    id2count = {id: 0 for id in id_list} # 유저id: 신고당한 횟수
    id2report = {id: [] for id in id_list} # 유저id : 신고한 id list
    ban_list = []
    for r in report:
        a, b = r.split() # 신고한 사람, 신고 당한 사람
        if b not in id2report[a]: # 중복 신고가 아니라면
            id2report[a].append(b)
            id2count[b] += 1
    for key, val in id2count.items():
        if val >= k:
            ban_list.append(key)
            
    for key, val in id2report.items():
        result = 0
        for i in val:
            if i in ban_list:
                result += 1
        answer.append(result)
    return answer