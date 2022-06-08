#220608 3109 빵집
# 우, 우상, 우하 이동
# 각 칸을 지나는 파이프 하나, 빈칸에만 파이프 가능
# 파이프라인의 최대 개수
# n = 10000*500
#
import copy
import sys
input = sys.stdin.readline

def dfs(sRow, sCol):
    global r, c, board, answer, visited, moves

    stack = [[sRow,sCol]]

    while stack:
        nowR, nowC = stack.pop()
        visited[nowR][nowC] = 1
        if nowC == c-1:
            answer += 1
            return
        for move in moves:
            nxtR = nowR + move[0]
            nxtC = nowC + move[1]
            if 0 <= nxtR < r and 0 <= nxtC < c:
                if visited[nxtR][nxtC] == 0 and board[nxtR][nxtC] == ".":
                    stack.append([nxtR,nxtC])
r, c = map(int,input().split())
board = [list(input())[:-1] for _ in range(r)]
# for kk in board:
#     print(kk)
# print("---------")
visited = [[0]*c for _ in range(r)]
moves = [[1,1],[0,1],[-1,1]]

answer = 0

for start in range(r):
    dfs(start,0)
# for kk in visited:
#     print(kk)

print(answer)