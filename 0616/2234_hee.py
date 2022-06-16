from collections import deque

def bfs(x, y):
    cnt = 1
    Q = deque([(x, y)])
    V[y][x] = True
    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + D[i][0]
            ny = y + D[i][1]
            if not int(G[y][x][i]) and not V[ny][nx]:
                V[ny][nx] = True
                Q.append((nx, ny))
                cnt += 1
    return cnt

N, M = map(int, input().split())
G = []

for _ in range(M):
    L = list(map(int, input().split()))
    temp = []
    for j in L:
        B = bin(j)[2:]
        while len(B) < 4:
            B = '0' + B
        temp.append(list(B))
    G.append(list(temp))

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

V = [[False] * N for _ in range(M)]
ans1, ans2, ans3 = 0, 0, 0
prev = 0
for y in range(M):
    for x in range(N):
        if not V[y][x]:
            ans1 += 1
            ans2 = max(ans2, bfs(x, y))
print(ans1)
print(ans2)

for y in range(M):
    for x in range(N):
        for i in range(4):
            if int(G[y][x][i]):
                V = [[False] * N for _ in range(M)]
                nx = x + D[i][0]
                ny = y + D[i][1]
                if -1 < nx < N and -1 < ny < M:
                    G[y][x][i] = '0'
                    ans3 = max(ans3, bfs(x, y))
                    G[y][x][i] = '1'
print(ans3)