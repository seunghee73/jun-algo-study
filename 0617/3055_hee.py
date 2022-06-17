import pprint
import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

D = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def water():
    global W

    Q = []
    for x, y in W:
        for d in D:
            nx = x + d[0]
            ny = y + d[1]
            if -1 < nx < C and -1 < ny < R and (G[ny][nx] == '.' or G[ny][nx] == 'S'):
                G[ny][nx] = '*'
                Q.append((nx, ny))
    W = list(Q)


def find():
    cnt = 0
    Q = deque([(0, S[0], S[1])])
    tempV = [[False] * C for _ in range(R)]
    tempV[S[1]][S[0]] = True

    while Q:
        c, x, y = Q.popleft()
        if cnt <= c:
            cnt += 1
            water()
        if [x, y] == E:
            print(c)
            return True

        for d in D:
            nx = x + d[0]
            ny = y + d[1]

            if -1 < nx < C and -1 < ny < R and (G[ny][nx] == '.' or G[ny][nx] == 'D') and not tempV[ny][nx]:
                tempV[ny][nx] = True
                Q.append((c + 1, nx, ny))


R, C = map(int, input().split())
G = []
W = []

for i in range(R):
    L = list(input().strip())
    G.append(L)

    for j in range(C):
        if L[j] == 'S':
            S = [j, i]
        elif L[j] == '*':
            W.append((j, i))
        elif L[j] == 'D':
            E = [j, i]

if not find():
    print('KAKTUS')