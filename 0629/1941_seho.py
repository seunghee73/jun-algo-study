#220626 1941 소문난 칠공주
# 5*5의 board에서... 7명의 서로 인접한 학생 그룹
# 중 이다솜파의 학생이 4명이상 포함된 경우의 수를 하라
# S 는 이다솜씨 파벌, Y는 임 도연씨 파벌
# 하 ^^.. 해당 문제에서 조합의 개ㅑ수는 25C7 이다 ^^.. 50C7인줄 ㅎㅎ;;
import sys
from collections import deque
from itertools import combinations

def bfs(getLst):
    global board, moves
    loc = [0]*7
    loc[0] = 1
    queue = deque([getLst[0]])

    while queue:
        now = queue.popleft()

        for move in moves:
            nxtR, nxtC = now[0] + move[0], now[1] + move[1]
            if 0 <= nxtR < 5 and 0 <= nxtC < 5:
                for idx in range(7):
                    if [nxtR,nxtC] == getLst[idx] and loc[idx] == 0:
                        loc[idx] = 1
                        queue.append([nxtR,nxtC])
    if sum(loc) == 7:
        return True
    else:
        return False


input = sys.stdin.readline

board = [list(input()) for _ in range(5)]
moves = [[1,0],[-1,0],[0,1],[0,-1]]
answer = 0

locs = [[r,c] for r in range(5) for c in range(5)]

for permu in list(combinations(locs,7)):
    sCnt = 0
    for per in permu:
        if board[per[0]][per[1]] == "S":
            sCnt += 1
    result = 0
    if sCnt >= 4:
        if bfs(permu):
            answer += 1
print(answer)