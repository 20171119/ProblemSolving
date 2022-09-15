t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i].append(temp[i*m+j])
    
    dp = [[0]*m for _ in range(n)]
    
    for i in range(n):
        dp[i][0] = arr[i][0]

    for i in range(n):
        for j in range(1,m):
            dp[i][j] = arr[i][j] + dp[i][j-1]
            if i-1 >= 0:
                dp[i][j] = max(dp[i][j], arr[i][j] + dp[i-1][j-1])
            if i+1 < n:
                dp[i][j] = max(dp[i][j], arr[i][j] + dp[i+1][j-1])
    
    print(max(dp[n-1]))