import sys
input = sys.stdin.readline

M, N = map(int, input().split())
G = [[1] * M for _ in range(M)]
p = [[0] * M for _ in range(M)]
t = [0] * (2 * M - 1)
for _ in range(N):
    a, b, c = map(int, input().split())
    for i in range(a, a + b):
        t[i] += 1
    for i in range(a + b, a + b + c):
        t[i] += 2

cnt = 0
for i in range(M - 1, -1, -1):
    tmp = t[cnt]
    cnt += 1
    p[i][0] = tmp
    G[i][0] += tmp
for i in range(1, M):
    tmp = t[cnt]
    cnt += 1
    p[0][i] = tmp
    G[0][i] += tmp

for i in range(1, M):
    for k in range(1, M):
        p[i][k] = max(p[i - 1][k - 1], p[i - 1][k], p[i][k - 1])
        G[i][k] += p[i][k]

for i in G:
    print(*i)
