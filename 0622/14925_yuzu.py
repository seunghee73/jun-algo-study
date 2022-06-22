m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[0]*n for _ in range(m)]
ans = 0
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0:
            if arr[i][j] == 0:
                dp[i][j] = 1
        else:
            if arr[i][j] == 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        ans = max(ans, dp[i][j])
print(ans)