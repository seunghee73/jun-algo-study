#220622 14295 목장 건설하기
# 직사각형의 board가 주어질때, 나무와 바위가 포함되지 않는 최대 크기의 정사각형 찾기
# m*n <= 1000*1000 = board
#
import sys
input = sys.stdin.readline

m, n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
visited = [[0]*(n) for _ in range(m)]
answer = 0

for r in range(m):
    if board[r][0] == 0:
        visited[r][0] = 1
for c in range(n):
    if board[0][c] == 0:
        visited[0][c] = 1

for r in range(1,m):
    for c in range(1,n):
        if board[r][c] == 0:
            visited[r][c] = min(visited[r-1][c], visited[r][c-1], visited[r-1][c-1]) + 1
for r in range(m):
    for c in range(n):
        answer = max(answer,visited[r][c])

print(answer)