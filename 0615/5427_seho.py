#220615 5427 불
# 불이 매초 마다 상하좌우로 퍼져간다.
# 상근이는 상하좌우 이동가능.
# 벽, 불이 옮겨진 칸 or 불이 붙으려는 칸 으로 이동 불가.
# 불이 옮겨옴과 동시에 다른 칸으로 이동 가능
# 2개 보드 사용? bfs?
# n ~ w*h <= 1,000,000
import copy
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global w, h, board, boardOnFire, time, moves, me, fires

    while 1:
        time += 1
        nxtMe = deque([])
        nxtFire = deque([])
        check = True

        # for a,b in zip(board, boardOnFire):
        #     print(a,"||",b)
        # print()
        for fire in fires:
            boardOnFire[fire[0]][fire[1]] = 1
            for move in moves:
                nxtFR = fire[0] + move[0]
                nxtFC = fire[1] + move[1]
                if 0 <= nxtFR < h and 0 <= nxtFC < w:
                    if board[nxtFR][nxtFC] in ["@","."]:
                        board[nxtFR][nxtFC] = "*"
                        nxtFire.append([nxtFR,nxtFC])

        for now in me:
            for move in moves:
                nxtR = now[0] + move[0]
                nxtC = now[1] + move[1]
                if 0 <= nxtR < h and 0 <= nxtC < w:
                    if board[nxtR][nxtC] == "." and boardOnFire[nxtR][nxtC] == 0:
                        board[nxtR][nxtC] = "@"
                        nxtMe.append([nxtR,nxtC])
                        check = False
                else:
                    print(time)
                    return

        if check:
            print("IMPOSSIBLE")
            return
        me = copy.deepcopy(nxtMe)
        fires = copy.deepcopy(nxtFire)

tc_num = int(input())
moves = [[0,1],[0,-1],[1,0],[-1,0]]
for tc in range(tc_num):
    time = 0
    w, h = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    # boardOnFire = [[0]*w for _ in range(h)]
    me = deque([])
    fires = deque([])
    for r in range(h):
        for c in range(w):
            if board[r][c] == "*":
                fires.append([r,c])
            elif board[r][c] == "@":
                me.append([r,c])
    bfs()

    # for a,b in zip(board, boardOnFire):
    #     print(a,"||",b)