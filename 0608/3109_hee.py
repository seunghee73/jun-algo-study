R, C = map(int, input().split())
G = []
def dfs(r, c, idx):
    if c == C-1 and not V[idx]:
        V[idx] = True
        return

    for d in D:
        nr = r + d[1]
        nc = c + d[0]
        if -1 < nr < R and -1 < nc < C and G[nr][nc] == '.' and not V[idx]:
            G[nr][nc] = 'x'
            dfs(nr, nc, idx)

for _ in range(R):
    G.append(list(input()))

V = [False] * R
D = [(1, -1), (1, 0), (1, 1)]
for i in range(R):
    dfs(i, 0, i)
print(sum(V))