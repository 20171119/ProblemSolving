# 해시
def solution(genres, plays):
    gdict = {} # {genre: play_sum} 형태의 dict ex) {'classic': 1450, 'pop': '3100'}
    grank = [] # genre 의 play_sum 이 높은 순서의 배열 ex) ['pop', 'classic']
    gpi = [] # [(genre, play, idx)] 순의 배열
    answer = []
    for i in range(len(genres)):
        gpi.append((genres[i], plays[i], i))
        gdict[genres[i]] = 0  # 미리 val 0으로 설정 안하면 더할수 없엇음. 다른 방법??
    for j in range(len(genres)):
        gdict[genres[j]] += plays[j]
    
    for i in range(len(gdict)):
        maxkey = max(gdict, key = gdict.get) # dict 중 가장 큰 key 값 가져옴
        grank.append(maxkey)
        del gdict[maxkey]

    gpi = sorted(gpi, key = lambda x : x[1], reverse = True) # play 높은 순서로 정렬\
    # gpi = [('pop', 2500, 4), ('classic', 800, 3), ('pop', 600, 1), ('classic', 500, 0), ('classic', 150, 2)]
    # grank = ['pop', 'classic']
    for g in grank:
        count = 0
        for i in range(len(gpi)):
            if count < 2:
                if gpi[i][0] == g:
                    count += 1
                    answer.append(gpi[i][2]) # answer에 idx 추가
            else:
                continue

    return answer