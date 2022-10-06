def solution(X, Y):
    result = []
    for s in list(set(X) & set(Y)):
        x_count = X.count(s)
        y_count = Y.count(s)
        for _ in range(min(x_count, y_count)):
            result.append(s)
    if not result: return "-1"
    if max(result) == "0": return "0"
    result.sort(reverse=True)
    return ''.join(result)