import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

t = int(input())
D = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def fire():
    global F

    Q = []
    for x, y in F:
        for d in D:
            nx = x + d[0]
            ny = y + d[1]
            if -1 < nx < w and -1 < ny < h and G[ny][nx] != '*' and G[ny][nx] != '#':
                G[ny][nx] = '*'
                Q.append((nx, ny))
    F = list(Q)


def find():
    cnt = 0
    Q = [(0, S[0], S[1])]
    tempV = [[False] * w for _ in range(h)]
    tempV[S[1]][S[0]] = True

    while Q:
        c, x, y = heapq.heappop(Q)
        if cnt <= c:
            cnt += 1
            fire()

        for d in D:
            nx = x + d[0]
            ny = y + d[1]
            if not (-1 < nx < w and -1 < ny < h):
                print(c + 1)
                return True

            elif G[ny][nx] == '.' and not tempV[ny][nx]:
                tempV[ny][nx] = True
                heapq.heappush(Q, (c + 1, nx, ny))


for _ in range(t):
    w, h = map(int, input().split())
    G = []
    F = []

    for i in range(h):
        L = list(input().strip())
        G.append(L)

        for j in range(w):
            if L[j] == '@':
                S = [j, i]
            elif L[j] == '*':
                F.append((j, i))

    if not find():
        print('IMPOSSIBLE')

