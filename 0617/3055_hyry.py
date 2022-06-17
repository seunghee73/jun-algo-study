import sys
from collections import deque
input = sys.stdin.readline


def flood():
    global waters

    tmp = deque()
    while waters:
        curR, curC = waters.popleft()

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and MAP[newR][newC] == '.':
                tmp.append((newR, newC))
                MAP[newR][newC] = '*'

    waters = tmp


def runAway():
    global hedgehog

    tmp = deque()
    while hedgehog:
        curR, curC = hedgehog.popleft()
        if MAP[curR][curC] == 'D':
            return visit[curR][curC] - 1

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C \
                    and not visit[newR][newC] and MAP[newR][newC] in ('.', 'D'):
                tmp.append((newR, newC))
                visit[newR][newC] = visit[curR][curC] + 1

    hedgehog = tmp
    return 0


R, C = map(int, input().rstrip().split())
MAP = [list(input().rstrip()) for _ in range(R)]

hedgehog = deque()
waters = deque()
visit = [[0] * C for _ in range(R)]
for row in range(R):
    for col in range(C):
        if MAP[row][col] == 'S':
            hedgehog.append((row, col))
            MAP[row][col] = '.'
            visit[row][col] = 1
        if MAP[row][col] == '*':
            waters.append((row, col))


while waters or hedgehog:
    if not hedgehog:
        print('KAKTUS')
        break
    flood()
    ans = runAway()
    if ans:
        print(ans)
        break