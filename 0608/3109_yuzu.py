r, c = map(int, input().split())
map = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

def dfs(x, y):
    dx = [-1, 0, 1]
    if y == c-1:
        return 1
    for i in range(3):
        nx = x+dx[i]
        ny = y+1
        if 0<=nx<r and 0<=ny<c and visited[nx][ny] == 0 and map[nx][ny] == '.':
            visited[nx][ny] = 1
            if dfs(nx, ny):
                return 1
    return 0

cnt = 0
for i in range(r):
    if dfs(i, 0):
        cnt += 1
print(cnt)