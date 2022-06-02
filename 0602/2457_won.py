import sys
input = sys.stdin.readline

N = int(input())
G = [0] * N
for i in range(N):
    a, b, c, d = map(int, input().split())
    # G[i][0], G[i][1] => 피는 날, 지는 날
    G[i] = [a * 100 + b, c * 100 + d]

ans = 0
now = 1201
# 피는날이 1130 큰 날 중에 가장 먼저 피는 날을 찾는다 => 갱신 후 반복
while now > 301:
    minV = 1232
    minIdx = 0
    for i in range(len(G)):
        if G[i][1] >= now and G[i][0] <= now:
            minV = min(minV, G[i][0])
            minIdx = i
    if now > minV:
        now = minV
        ans += 1
        del G[minIdx]
    else:
        ans = 0
        break
print(ans)
