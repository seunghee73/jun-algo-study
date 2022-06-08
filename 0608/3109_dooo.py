dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(sx, sy):
    global cnt, flag
    v[sx][sy] = 1
    if sy == m-1:
        cnt += 1
        flag = 1

        return
    for i in range(3):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < n and 0 <= ny <m and arr[nx][ny] == '.' and v[nx][ny] == 0:
            v[nx][ny] = 1
            dfs(nx, ny)
            if flag == 1:
                return



n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
v = [[0] * m for _ in range(n)]
cnt = 0
for i in range(n):
    flag = 0
    dfs(i, 0)

print(cnt)