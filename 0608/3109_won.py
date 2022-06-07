import sys
input = sys.stdin.readline

dr = [-1, 0, 1]
dc = [1, 1, 1]

R, C = map(int, input().split())
G = [input().rstrip() for _ in range(R)]

def dfs(sr, sc):
    if sc == C - 1:
        return True
    for d in range(3):
        nr, nc = sr + dr[d], sc + dc[d]
        if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == '.' and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            if dfs(nr, nc):
                return True
    return False

ans = 0
visited = [[0] * C for _ in range(R)]
for i in range(R):
    if G[i][0] == '.':
        visited[i][0] = 1
        if dfs(i, 0):
            ans += 1

print(ans)
