import sys
input = sys.stdin.readline

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input().rstrip())

def bfs():
    visited = [[0] * w for _ in range(h)]
    qu = deque()
    for i in range(h):
        for k in range(w):
            if G[i][k] == '*':  # 불
                qu.append([i, k])
                visited[i][k] = '*'
            elif G[i][k] == '@':  # 상근
                visited[i][k] = 1
                sang = [i, k]
    qu.append(sang)
    while qu:
        cr, cc = qu.popleft()
        if visited[cr][cc] != '*' and (cr == h - 1 or cc == w - 1 or cr == 0 or cc == 0):
            return visited[cr][cc]

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if visited[nr][nc] == 0 and (G[nr][nc] == '.' or G[nr][nc] == '@'):
                if visited[cr][cc] == '*':  # 불이면
                    visited[nr][nc] = '*'
                else:  # 상근
                    visited[nr][nc] = visited[cr][cc] + 1
                qu.append([nr, nc])

    return 'IMPOSSIBLE'

for _ in range(T):
    w, h = map(int, input().split())
    G = [list(input().rstrip()) for _ in range(h)]
    ans = bfs()
    print(ans)
