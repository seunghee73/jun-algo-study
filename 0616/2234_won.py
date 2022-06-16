import sys
input = sys.stdin.readline
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

M, N = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for k in range(M):
        tmp = bin(G[i][k])[2:]
        if len(tmp) < 4:
            tmp = '0' * (4 - len(tmp)) + tmp
        G[i][k] = tmp

visited = [[0] * M for _ in range(N)]

def f(sr, sc):
    cnt = 1
    qu = deque()
    qu2 = []
    qu2.append([sr, sc])
    qu.append([sr, sc])
    visited[sr][sc] = 1
    while qu:
        cr, cc = qu.popleft()

        for d in range(4):
            if G[cr][cc][d] == '0':
                nr, nc = cr + dr[d], cc + dc[d]

                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue

                if visited[nr][nc] == 0:
                    qu.append([nr, nc])
                    qu2.append([nr, nc])
                    visited[nr][nc] = visited[cr][cc] + 1
                    cnt += 1
    for cr, cc in qu2:
        visited[cr][cc] = cnt
    return cnt

cnt1 = 0
cnt2 = 0
for i in range(N):
    for k in range(M):
        if visited[i][k] == 0:
            cnt1 += 1
            res = f(i, k)
            cnt2 = max(cnt2, res)

ans = 0
for i in range(N):
    for k in range(M):
        tmp = list(G[i][k])
        for d in range(4):
            if tmp[d] == '1':
                tmp[d] = '0'
                G[i][k] = ''.join(tmp)
                visited = [[0] * M for _ in range(N)]
                res = f(i, k)
                ans = max(ans, res)
                tmp[d] = '1'
                G[i][k] = ''.join(tmp)

print(cnt1)
print(cnt2)
print(ans)
