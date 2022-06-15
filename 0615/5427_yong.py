# bfs문제 먼저 불이 갈 수 있는 모든 곳을 bfs로 탐색해 시간으로 표시
# 상근이가 이동할 장소가 불이 붙는 시간보다 빠르면 지나갈 수 있다고 판단
# 상근이가 벽에 도달하면 탈출 성공!

from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def f_bfs():
    while fire:
        y, x = fire.popleft()
        for dy, dx in d:
            if 0 <= y+dy < h and 0 <= x+dx < w:
                if arr[y+dy][x+dx] != '#' and (not arr[y+dy][x+dx] or arr[y+dy][x+dx] > arr[y][x]+1):
                    arr[y+dy][x+dx] = arr[y][x] + 1
                    fire.append((y+dy, x+dx))        

def s_bfs():
    global ans
    arr[sang[0][0]][sang[0][1]] = 1
    if sang[0][0] == 0 or sang[0][0] == h-1 or sang[0][1] == 0 or sang[0][1] == w-1:
        ans = 1
        return True
    while sang:
        y, x = sang.popleft()
        for dy, dx in d:
            if 0 <= y+dy < h and 0 <= x+dx < w:
                if arr[y+dy][x+dx] != '#' and (arr[y+dy][x+dx] > arr[y][x] + 1 or not arr[y+dy][x+dx]):
                    arr[y+dy][x+dx] = arr[y][x] + 1
                    if y+dy == 0 or x+dx == 0 or y+dy == h-1 or x+dx == w-1:
                        ans = arr[y+dy][x+dx]
                        return True
                    sang.append((y+dy, x+dx))
    return False

T = int(input())

for _ in range(T):
    ans = 0
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    fire = deque()
    sang = deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire.append((i, j))
                arr[i][j] = 1
            if arr[i][j] == '@':
                sang.append((i, j))
                arr[i][j] = 0
            if arr[i][j] == '.':
                arr[i][j] = 0
    f_bfs()
    if s_bfs():
        print(ans)
    else:
        print('IMPOSSIBLE')