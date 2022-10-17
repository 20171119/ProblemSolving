from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque([])
    for city in cities:
        city = city.lower()
        if city not in q:
            answer += 5
            q.append(city)
            if len(q) > cacheSize:
                q.popleft()
        else:
            answer += 1
            q.remove(city)
            q.append(city)
    return answer

# 다른 사람 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time