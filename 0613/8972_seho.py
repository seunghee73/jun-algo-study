#2206013 8972 미친 아두이노
# r*c 의 board
# steps of 5 repeating
# R = crazy, I = you
# r,c <= 100
# moveCommand만큼 이동진행
# me 먼저이동 -> (아두이노 만나면 gaveover) -> crazy 이동 -> (me랑 crazy만나면 gameover)
# 3, 4 crazy 갯수 만큼 반복.
# crazy 들이동시 서로 만나면 서로 삭제
import copy
import sys
from collections import deque
input = sys.stdin.readline

def gameStart():
    global r, c, crazyAduino, me, moves, moveCommand
    visited = [[0]*(c) for _ in range(r)]
    for idx in range(len(moveCommand)):
        # 종수 이동
        me = [me[0]+moves[moveCommand[idx]-1][0],me[1]+moves[moveCommand[idx]-1][1]]
        for aduino in crazyAduino:
            if me[0] == aduino[0] and me[1] == aduino[1]:
                print("kraj {0}".format(idx+1))
                return

        # 아두이노 이동
        tempAduino = set()
        deleteAduino = set()
        for crazyIdx in range(len(crazyAduino)):
            [AduR,AduC] = crazyAduino[crazyIdx]
            moveMin = float('inf')

            for moveIdx in range(len(moves)):
                nxtAduR = crazyAduino[crazyIdx][0] + moves[moveIdx][0]
                nxtAduC = crazyAduino[crazyIdx][1] + moves[moveIdx][1]
                if 0 <= nxtAduR < r and 0 <= nxtAduC < c:
                    if moveMin > abs(me[0]-nxtAduR)+abs(me[1]-nxtAduC):
                        moveMin = abs(me[0] - nxtAduR) + abs(me[1] - nxtAduC)
                        AduR = nxtAduR
                        AduC = nxtAduC
            if AduR == me[0] and AduC == me[1]:
                print("kraj {0}".format(idx + 1))
                return
            if (AduR,AduC) in tempAduino:
                deleteAduino.add((AduR,AduC))
            else:
                tempAduino.add((AduR, AduC))

        crazyAduino = list(tempAduino-deleteAduino)


    answer = [["."]*c for _ in range(r)]
    answer[me[0]][me[1]] = "I"
    for idx in range(len(crazyAduino)):
        caIdx = crazyAduino[idx]
        answer[caIdx[0]][caIdx[1]] = "R"

    for ans in answer:
        print("".join(ans))
r, c = map(int,input().split())
crazyAduino = deque([])
me = []
for rIdx in range(r):
    get = list(input()[:-1])
    for cIdx in range(c):
        if get[cIdx] == "R":
            crazyAduino.append([rIdx,cIdx])
        elif get[cIdx] == "I":
            me = [rIdx,cIdx]
moves = [[1,-1],[1,0],[1,1],[0,-1],[0,0],[0,1],[-1,-1],[-1,0],[-1,1]]

moveCommand = list(map(int,list(input()[:-1])))
gameStart()