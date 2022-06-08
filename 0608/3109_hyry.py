import sys
input = sys.stdin.readline


def dfs(sR, sC):
    ST = [(sR, sC)]

    while ST:
        curR, curC = ST.pop()
        visit[curR][curC] = True
        if curC == C - 1: return True

        for dr, dc in ((1, 1), (0, 1), (-1, 1)): 
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and not visit[newR][newC] and MAP[newR][newC] == '.':
                ST.append((newR, newC))

    return False


R, C = map(int, input().rstrip().split())
MAP = [list(input().rstrip()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]

cnt = 0
for row in range(R):
    visit[row][0] = True
    if dfs(row, 0):
        cnt += 1

print(cnt)