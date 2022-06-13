# 조건을 활용한 구현문제
# R지점의 좌표를 갱신할 때 시간초과하는 문제점이 발생
# 좌표 저장을 딕셔너리로 바꿔 좌표를 key로 활용하여 시간을 줄였음

d = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

def I_Move(num):
    global I_idx
    y, x = I_idx
    dy = d[int(num)-1][0]
    dx = d[int(num)-1][1]
    if 0 <= y+dy < R and 0 <= x+dx < C:
        if arr[y+dy][x+dx] == 'R':
            return False
        else:
            arr[y][x] = '.'
            arr[y+dy][x+dx] = 'I'
            I_idx = [y+dy, x+dx]
            return True

def R_Move():
    global R_idx
    M_idx = {}
    for i in range(len(R_idx)):
        y, x = R_idx[i]
        arr[y][x] = '.'
        minV = 10000000000000
        ny = -1
        nx = -1
        for dy, dx in d:
            if 0 <= y+dy < R and 0 <= x+dx < C:
                if abs(I_idx[0] - (y+dy)) + abs(I_idx[1] - (x+dx)) < minV:
                    minV = abs(I_idx[0] - (y+dy)) + abs(I_idx[1] - (x+dx))
                    ny = y+dy
                    nx = x+dx
        if (ny, nx) in M_idx.keys():
            M_idx[(ny, nx)] += 1
        else:
            M_idx[(ny, nx)] = 1
        if arr[ny][nx] == 'I':
            return False
    coor = []
    for idx in M_idx.keys():
        y, x = idx
        if M_idx[idx] == 1:
            coor.append(idx)
            arr[y][x] = 'R'
        else:
            arr[y][x] = '.'
    R_idx = coor
    return True

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
I_idx = []
R_idx = []
M = input()
for i in range(len(M)):
    if i == 0:
        for j in range(R):
            for k in range(C):
                if arr[j][k] == 'I':
                    I_idx = [j, k]
                if arr[j][k] == 'R':
                    R_idx.append((j, k))
    if not I_Move(M[i]):
        print(f'kraj {i + 1}')
        exit()
    if not R_Move():
        print(f'kraj {i+1}')
        exit()

for i in range(R):
    for j in range(C):
        print(arr[i][j], end='')
    print()