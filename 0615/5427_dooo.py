from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, fire):
    q = deque()
    q.append((sx, sy))
    p = [[0] *m for _ in range(n)]
    p[sx][sy] = 1

    while q:
        time = deque()

        while q:
            cx, cy = q.popleft()
            if arr[cx][cy] == '*':
                continue
            if cx == 0 or cx == n-1 or cy == 0 or cy == m-1:

                return p[cx][cy]
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0<=nx<n and 0<=ny<m and p[nx][ny] == 0 and arr[nx][ny] == '.':
                    arr[nx][ny] = '@'
                    arr[cx][cy] = '.'
                    p[nx][ny] = p[cx][cy] + 1
                    time.append((nx,ny))
        q = time
        time = deque()
        while fire:
            fcx, fcy = fire.popleft()
            for i in range(4):
                fnx = fcx + dx[i]
                fny = fcy + dy[i]
                if 0<=fnx<n and 0<=fny<m and v[fnx][fny] == 0 and arr[fnx][fny] != '#':

                    arr[fnx][fny] = '*'
                    v[fnx][fny] = 1
                    time.append((fnx, fny))
        fire = time
    return 'IMPOSSIBLE'

TC = int(input())
for _ in range(TC):
    m, n = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    fire = deque()
    v = [[0] * m for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                sx = i
                sy = j
                flag = 1
            elif arr[i][j] =='*':
                v[i][j]= 1
                fire.append((i,j))
    print(bfs(sx, sy, fire))