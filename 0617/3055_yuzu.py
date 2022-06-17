r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
ss = []
water = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            ss.append((i, j))
        elif arr[i][j] == '*':
            water.append((i, j))

def bfs():
    ans = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while ss:
        for i in range(len(water)):
            wx, wy = water.pop(0)
            for j in range(4):
                nwx = wx+dx[j]
                nwy = wy+dy[j]
                if 0<=nwx<r and 0<=nwy<c:
                    if arr[nwx][nwy] == '.' and visit[nwx][nwy] == 0:
                        water.append((nwx, nwy))
                        arr[nwx][nwy] = '*'
                        visit[nwx][nwy] = 1
        ans += 1

        for i in range(len(ss)):
            sx, sy = ss.pop(0)
            for j in range(4):
                nsx = sx+dx[j]
                nsy = sy+dy[j]
                if 0<=nsx<r and 0<=nsy<c:
                    if arr[nsx][nsy] == '.' and visit[nsx][nsy] == 0:
                        ss.append((nsx, nsy))
                        visit[nsx][nsy] = 1
                    elif arr[nsx][nsy] == 'D':
                        return ans
    return

ans = bfs()
print(ans) if ans else print('KAKTUS')