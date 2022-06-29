import sys
input = sys.stdin.readline

# dfs를 활용한 경우의 수 탐색
# 한 좌표를 기준으로 상하좌우를 탐색, 가능한 경우의 수를 재귀를 통해 찾는다.

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def dfs(lst, cnt, Y):
    if Y > 3:
        return
    if cnt == 7:
        lst.sort()
        ans.add(tuple(lst))
    else:
        st = []
        for y, x in lst:
            for dy, dx in d:
                if 0 <= y + dy < 5 and 0 <= x + dx < 5 and (y+dy, x+dx) not in lst:
                    st.append((y+dy, x+dx))

        for y, x in st:
            if arr[y][x] == 'Y':
                dfs(lst + [(y, x)], cnt+1, Y+1)
            else:
                dfs(lst + [(y, x)], cnt+1, Y)

arr = [list(input().strip()) for _ in range(5)]
ans = set()
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'Y':
            dfs([(i, j)], 1, 1)
        else:
            dfs([(i, j)], 1, 0)
print(len(ans))
