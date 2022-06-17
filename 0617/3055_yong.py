# 물이 흐르는 곳을 먼저 bfs로 탐색
# 고슴도치가 물이 오기전에 갈 수 있는 곳을 찾아 탐색하며 D를 발견 시 횟수 출력

from collections import deque

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def w_bfs():
    while water:
        y, x = water.popleft()
        for dy, dx in d:
            if 0 <= y+dy < R and 0 <= x+dx < C:
                if not arr[y+dy][x+dx]:
                    arr[y+dy][x+dx] = arr[y][x] + 1
                    water.append((y+dy, x+dx))

def S_bfs():
    arr[S[0][0]][S[0][1]] = 1
    while S:
        y, x = S.popleft()
        for dy, dx in d:
            if 0 <= y + dy < R and 0 <= x + dx < C:
                if arr[y+dy][x+dx] == 'X':
                    continue
                if arr[y+dy][x+dx] == 'D':
                    return print(arr[y][x])
                if not arr[y+dy][x+dx] or arr[y+dy][x+dx] > arr[y][x] + 1:
                    arr[y+dy][x+dx] = arr[y][x] + 1
                    S.append((y+dy, x+dx))
    return print('KAKTUS')




R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
water = deque()
S = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            S.append((i, j))
            arr[i][j] = 0
        if arr[i][j] == '*':
            water.append((i, j))
            arr[i][j] = 1
        if arr[i][j] == '.':
            arr[i][j] = 0
w_bfs()
S_bfs()
