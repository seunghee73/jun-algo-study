M,N = map(int,input().split())
road = []
for _ in range(M):
    road.append(input().split())

dp = [[0]*N for _ in range(M)]

result=0

for i in range(N):
    if road[0][i] == '0':
        dp[0][i] = 1
        result = 1
for i in range(M):
    if road[i][0] == '0':
        dp[i][0] = 1
        result =1

for y in range(1,M):
    for x in range(1,N):
        if road[y][x] == '0':
            dp[y][x] = min(dp[y-1][x-1],dp[y-1][x],dp[y][x-1]) + 1
            if dp[y][x] > result:
                result = dp[y][x]

print(result)