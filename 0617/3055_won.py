import sys
input = sys.stdin.readline
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

R, C = map(int, input().split())
G = [list(input().rstrip()) for _ in range(R)]

qu = deque()
visited = [[0] * C for _ in range(R)]
start = [-1, -1]
for i in range(R):
    for k in range(C):
        if G[i][k] == '*':
            qu.append([i, k])
            visited[i][k] = '*'
        elif G[i][k] == 'S':
            visited[i][k] = 1
            start = [i, k]
qu.append(start)


def f(qu):
    while qu:
        cr, cc = qu.popleft()
        if visited[cr][cc] != '*' and G[cr][cc] == 'D':
            return visited[cr][cc] - 1

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if visited[nr][nc] == 0:
                if visited[cr][cc] == '*':  # 물
                    if G[nr][nc] == '.' or G[nr][nc] == 'S':
                        visited[nr][nc] = '*'
                        qu.append([nr, nc])
                else:  # 고슴도치
                    if G[nr][nc] == '.' or G[nr][nc] == 'D':
                        visited[nr][nc] = visited[cr][cc] + 1
                        qu.append([nr, nc])
    return 'KAKTUS'

ans = f(qu)
print(ans)
