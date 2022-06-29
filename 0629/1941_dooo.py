dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(lst , cnt, s, y):

    if y > 3:
        return
    if cnt == 6:
        lst.sort()
        ans.add(tuple(lst))
    else:
        st = []
        for n in range(len(lst)):
            for i in range(4):
                nx = lst[n][0] + dx[i]
                ny = lst[n][1] + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and (nx,ny) not in lst:

                    st.append((nx, ny))
        for nnx, nny in st:
            if arr[nnx][nny] == 'S':
                dfs(lst+[(nnx, nny)], cnt+1, s+1, y)
            else:
                dfs(lst+[(nnx, nny)], cnt + 1, s, y+1)
arr = [list(input()) for _ in range(5)]
ans = set()
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            dfs([(i, j)], 0, 0, 0)
print(len(ans))