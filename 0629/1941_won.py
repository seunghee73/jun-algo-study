import sys
input = sys.stdin.readline
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
G = [input().rstrip() for _ in range(5)]

def check():
    visited = [[0] * 5 for _ in range(5)]
    for i in path:
        visited[i // 5][i % 5] = 1
    qu = deque()
    qu.append(path[0])
    visited[path[0] // 5][path[0] % 5] = 0
    cnt = 1
    while qu:
        num = qu.popleft()
        cr, cc = num // 5, num % 5
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] == 1:
                visited[nr][nc] = 0
                qu.append(nr * 5 + nc)
                cnt += 1

    if cnt == 7:
        return True
    else:
        return False

def f(depth, yCnt, num):
    global ans
    if depth == 7 and yCnt <= 3:
        if check():
            ans += 1
        return
    if depth > 7 or yCnt >= 4 or num >= 25:
        return

    path.append(num)
    cr, cc = num // 5, num % 5
    if G[cr][cc] == 'Y':
        f(depth + 1, yCnt + 1, num + 1)
    else:
        f(depth + 1, yCnt, num + 1)
    path.pop()
    f(depth, yCnt, num + 1)
    return

ans = 0
path = []
f(0, 0, 0)
print(ans)
