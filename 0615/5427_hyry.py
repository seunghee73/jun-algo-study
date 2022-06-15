import sys
from collections import deque
input = sys.stdin.readline


def fireBfs():
    global fire

    tmp = deque()
    while fire:
        curR, curC = fire.popleft()

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc

            if 0 <= newR < R and 0 <= newC < C and MAP[newR][newC] == '.':
                tmp.append((newR, newC))
                MAP[newR][newC] = '*'
    fire = tmp


def personBfs():
    global person

    tmp = deque()
    while person:
        perR, perC = person.popleft()
        if perR in (0, R - 1) or perC in (0, C - 1) and MAP[perR][perC] == '.':
            return visit[perR][perC]

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newPR, newPC = perR + dr, perC + dc
            if 0 <= newPR < R and 0 <= newPC < C and MAP[newPR][newPC] == '.' and not visit[newPR][newPC]:
                tmp.append((newPR, newPC))
                visit[newPR][newPC] = visit[perR][perC] + 1
                if newPR in (0, R - 1) or newPC in (0, C - 1):
                    return visit[newPR][newPC]
    person = tmp
    return 0


def solution():
    global fire, person

    while fire or person:
        if not person: return "IMPOSSIBLE"
        if fire:
            fireBfs()
        ans = personBfs()
        if ans: return ans

    return "IMPOSSIBLE"


T = int(input().rstrip())
for _ in range(T):
    C, R = map(int, input().rstrip().split())
    MAP = [list(input().rstrip()) for _ in range(R)]
    visit = [[0] * C for _ in range(R)]

    fire = deque()
    person = deque()
    for row in range(R):
        for col in range(C):
            if MAP[row][col] == '@':
                person.append((row, col))
                visit[row][col] = 1
                MAP[row][col] = '.'
            if MAP[row][col] == '*':
                fire.append((row, col))

    print(solution())


'''
1
5 5
.....
...@.
###..
###..
#*#..

1
5 5
#####
#.*.@
#####
###..
#*#..
'''