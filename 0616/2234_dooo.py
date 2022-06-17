from collections import deque
dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = 1
    cnt = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx < n and 0<=ny<m and v[nx][ny] == 0:
                if i == 0:
                    if 1 & arr[cx][cy]:
                        continue
                elif i == 1:
                    if 2 & arr[cx][cy]:
                        continue
                elif i == 2:
                    if 4 & arr[cx][cy]:
                        continue
                elif i == 3:
                    if 8 & arr[cx][cy]:
                        continue
                v[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
cnt_lst = []
for i in range(n):
    for j in range(m):
        if v[i][j] == 0:
            res = bfs(i,j)
            cnt_lst.append(res)
break_lst = []
for i in range(n):
    for j in range(m):
        num = 1
        while num < 9:
            if num & arr[i][j]:
                v = [[0] * m for _ in range(n)]
                arr[i][j] -= num
                break_lst.append(bfs(i, j))
                arr[i][j] += num
            num *= 2
print(len(cnt_lst))
print(max(cnt_lst))
print(max(break_lst))


