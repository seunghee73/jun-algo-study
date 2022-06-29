arr = [list(input()) for _ in range(5)]
lst = []
ans = 0

def check(x, y, visit):
    for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        nx = x+dx
        ny = y+dy
        if 0<=nx<5 and 0<=ny<5 and visit[nx][ny] == 0:
            if (nx, ny) in lst:
                visit[nx][ny] = 1
                check(nx, ny, visit)

def dfs(depth, doyeon, x, y):
    global ans
    if doyeon > 3:
        return

    if depth == 7:
        visit = [[0] * 5 for _ in range(5)]
        sx, sy = lst[0][0], lst[0][1]
        visit[sx][sy] = 1
        check(sx, sy, visit)
        cnt = 0
        for i in range(5):
            cnt += sum(visit[i])
        if cnt == 7:
            ans += 1
        return

    if x == 5:
        return

    if arr[x][y] == 'Y':
        lst.append((x, y))
        if y == 4:
            dfs(depth+1, doyeon+1, x+1, 0)
        else:
            dfs(depth+1, doyeon+1, x, y+1)
        lst.pop()
    else:
        lst.append((x, y))
        if y == 4:
            dfs(depth+1, doyeon, x+1, 0)
        else:
            dfs(depth+1, doyeon, x, y+1)
        lst.pop()
    if y == 4:
        dfs(depth, doyeon, x+1, 0)
    else:
        dfs(depth, doyeon, x, y+1)

dfs(0, 0, 0, 0)
print(ans)