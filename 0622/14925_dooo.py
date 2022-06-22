n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
    if arr[i][0] == 0:
        dp[i][0] = 1
for j in range(m):
    if arr[0][j] == 0:
        dp[0][j] = 1
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
ans = 0
for lst in dp:
    ans = max(ans, max(lst))
print(ans)