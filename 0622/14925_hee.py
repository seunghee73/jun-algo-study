M, N = map(int, input().split())
G = []
for _ in range(M):
    G.append(list(map(int, input().split())))

DP = [[0] * N for _ in range(M)]
ans = 0
for y in range(M):
    for x in range(N):
        if G[y][x] == 0:
            if x == 0 or y == 0:
                DP[y][x] = 1
            else:
                DP[y][x] = min(DP[y - 1][x], DP[y - 1][x - 1], DP[y][x - 1]) + 1
            ans = max(DP[y][x], ans, 1)
print(ans)