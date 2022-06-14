import copy
dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
direct = list(map(int, input()))

def move(arr, direct, n, m):
    global flag
    nx = 0
    ny = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'I':
                nx = i
                ny = j
                break

    for i in range(len(direct)):
        movearr = [['.' for _ in range(m)] for _ in range(n)]
        nx = nx + dx[direct[i]]
        ny = ny + dy[direct[i]]
        movearr[nx][ny] = 'I'
        if arr[nx][ny] == 'R':
            flag = 1
            return i+1

        for r in range(n):
            for c in range(m):
                if arr[r][c] == 'R':
                    dist = [999]
                    for mm in range(1,10):
                        mx = r + dx[mm]
                        my = c + dy[mm]
                        dist.append(abs(nx-mx)+abs(ny-my))
                    d = dist.index(min(dist))
                    x = r + dx[d]
                    y = c + dy[d]
                    if movearr[x][y] == 'I':
                        flag = 1
                        return i+1
                    elif movearr[x][y] == '.':
                        movearr[x][y] = 'R'
                    else:
                        movearr[x][y] = 'X'
        for j in range(n):
            for k in range(m):
                if movearr[j][k] == 'X':
                    movearr[j][k] = '.'
        arr = copy.deepcopy(movearr)

    return arr
flag=0
ans = move(arr, direct, n, m)
if flag == 1:
    print('kraj {}'.format(ans))
else:
    for i in ans:
        for j in i:
            print(j, end= '')
        print()