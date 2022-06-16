#220617 3055 탈출
# r*c  < 50*50
# S move to D
# 물이 인접칸에 차게됨
# 고슴도치는 물이 찰 예정인 칸에는 이동 불가
# 고슴도치 이동

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    global r, c, board, queue, cave, visited
    moves = [[0,1],[0,-1],[1,0],[-1,0]]

    while queue:
        now = queue.popleft()

        for move in moves:
            nxtR = now[0] + move[0]
            nxtC = now[1] + move[1]
            if 0 <= nxtR < r and 0 <= nxtC < c:
                if visited[now[0]][now[1]] == "*":
                    if board[nxtR][nxtC] not in ["X","D"] and visited[nxtR][nxtC] != "*":
                        visited[nxtR][nxtC] = "*"
                        queue.append([nxtR,nxtC])
                else:
                    if board[nxtR][nxtC] == "D":
                        print(visited[now[0]][now[1]] + 1)
                        exit()
                    if board[nxtR][nxtC] =="." and visited[nxtR][nxtC] == -1:
                        visited[nxtR][nxtC] = visited[now[0]][now[1]] + 1
                        queue.append([nxtR,nxtC])
    print("KAKTUS")

r, c = map(int,input().split())
board = [list(input().rstrip()) for _ in range(r)]


me = []
queue = []
visited = [[-1]*(c) for _ in range(r)]
cave = []

for row in range(r):
    for col in range(c):
        if board[row][col] == "D":
            cave = [row,col]
        elif board[row][col] == "S":
            me = [row,col]
            visited[row][col] = 0
        elif board[row][col] == "*":
            queue.append([row,col])
            visited[row][col] = "*"
queue.insert(0,me)
queue = deque(queue)

bfs()