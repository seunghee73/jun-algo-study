import sys
input = sys.stdin.readline
# from collections import deque

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
ans = 0

for i in range(1, N + 1):
    for k in range(1, M + 1):
        if G[i - 1][k - 1] == 0:
            dp[i][k] = min(dp[i - 1][k - 1], dp[i - 1][k], dp[i][k - 1]) + 1
            ans = max(ans, dp[i][k])
print(ans)
