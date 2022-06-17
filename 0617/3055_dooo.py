from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, waters):

    q = deque()
    v = [[0] * m for _ in range(n)]
    q.append((sx, sy))
    vw = [[0]*m for _ in range(n)]
    v[sx][sy] = 1
    while q:
        time = deque()
        while waters:
            fsx, fsy = waters.popleft()
            for i in range(4):
                fnx = fsx + dx[i]
                fny = fsy + dy[i]
                if 0 <= fnx < n and 0 <= fny < m and arr[fnx][fny] == '.' and vw[fnx][fny] == 0:
                    arr[fnx][fny] = '*'
                    vw[fnx][fny] = 1
                    time.append((fnx, fny))
        waters = time

        time = deque()
        while q:
            cx, cy = q.popleft()
            if cx == ex and cy == ey:
                return v[cx][cy] -1
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and (arr[nx][ny] == '.' or arr[nx][ny] == 'D'):
                    arr[nx][ny] = 'S'
                    arr[cx][cy] = '.'
                    v[nx][ny] = v[cx][cy] + 1
                    time.append((nx, ny))
        q = time
    return 'KAKTUS'

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
waters = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            sx = i
            sy = j
        elif arr[i][j] == '*':
            waters.append((i, j))
        elif arr[i][j] == 'D':
            ex = i
            ey = j
ans = bfs(sx, sy, waters)
print(ans)