#2206013 2234 성곽
# 방의 개수, 가장 넓은 방의 넚이, 이웃한 두 방의 넓이 합 출력
# m*n <= 50*50
# 서 0001/ 북 0010/ 동 0100/ 님 1000 의 값이 각 칸에 더해진다.\
# 비트 연산자로 알수있을듯.

import sys

input = sys.stdin.readline

def dfs(r,c):
    global n, m, board, visited, rooms
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    stack = [[r,c]]

    roomNum = int(list(rooms.keys())[-1])+1
    visited[r][c] = roomNum
    rooms[str(roomNum)] = 1
    while stack:
        now = stack.pop()
        toBin = bin(board[now[0]][now[1]])
        toBin = "0" * (4 - len(toBin[2:])) + toBin[2:]
        for idx in range(len(toBin)):
            if int(toBin[idx]) == 0:
                nxtR = now[0] + moves[idx][0]
                nxtC = now[1] + moves[idx][1]
                if 0 <= nxtR < m and 0 <= nxtC < n:
                    if visited[nxtR][nxtC] == 0:
                        stack.append([nxtR,nxtC])
                        visited[nxtR][nxtC] = roomNum
                        rooms[str(roomNum)] += 1

n, m = map(int,input().split())
board = []
for _ in range(m):
    board.append(list(map(int,input().split())))
visited = [[0]*n for _ in range(m)]
rooms = {"0":0} # 방의 넓이

for r in range(m):
    for c in range(n):
        if visited[r][c] == 0:
            dfs(r,c)

# for kk in visited:
#     print(kk)
# print(rooms)
print(len(rooms.keys())-1)
print(max(rooms.values()))
answer2 = 0

for r in range(m):
    for c in range(n):
        if c+1 < n:
            if visited[r][c] != visited[r][c+1]:
                answer2 = max(answer2,rooms[str(visited[r][c])]+rooms[str(visited[r][c+1])])
        if r + 1 < m:
            if visited[r][c] != visited[r+1][c]:
                answer2 = max(answer2,rooms[str(visited[r][c])]+rooms[str(visited[r+1][c])])
print(answer2)