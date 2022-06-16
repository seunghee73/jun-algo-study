# 영역의 넓이구하고 이용하는 dfs문제
# 벽에 대한 정보는 리스트를 활용하여 저장
# 영역을 탐색하며 아직 방문하지 않은 지역에 dfs를 활용 전체 넓이를 계산 후 저장
# 매 함수 실행마다 cnt카운트를 올려 방의 개수 계산
# dfs실행시마다 cnt를 활용하여 저장한 넓이에 해당하는 인덱스로 갱신
# 갱신된 정보를 탐색하여 다른 인덱스와 붙어있다면 해당 인덱스의 넓이끼리 합을 계산하여 합의 최대 구하기

wall = [
    [(1, 0), (-1, 0), (0, 1), (0, -1)],
    [(1, 0), (-1, 0), (0, 1)],
    [(1, 0), (0, 1), (0, -1)],
    [(1, 0), (0, 1)],
    [(1, 0), (-1, 0), (0, -1)],
    [(1, 0), (-1, 0)],
    [(1, 0), (0, -1)],
    [(1, 0)],
    [(-1, 0), (0, 1), (0, -1)],
    [(-1, 0), (0, 1)],
    [(0, 1), (0, -1)],
    [(0, 1)],
    [(-1, 0), (0, -1)],
    [(-1, 0)],
    [(0, -1)],
    [],
]

def dfs(y, x):
    global maxV
    global cnt
    stack = [(y, x)]
    val = 1
    while stack:
        y, x = stack.pop()
        if visited[y][x]:
            continue
        visited[y][x] = val
        val += 1
        for dy, dx in wall[arr[y][x]]:
            if 0 <= y+dy < M and 0 <= x+dx < N and not visited[y+dy][x+dx]:
                stack.append((y+dy, x+dx))
        arr[y][x] = cnt
    Vol.append(val-1)



N, M = map(int, input().split())
cnt = 0
Vol = []
arr = [list(map(int, input().split())) for _ in range(M)]
maxV = 0
visited = [[0] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt)
print(max(Vol))
for i in range(M):
    for j in range(N):
        for di, dj in wall[0]:
            if 0 <= i+di < M and 0 <= j+dj < N and arr[i][j] != arr[i+di][j+dj]:
                if Vol[arr[i][j]] + Vol[arr[i+di][j+dj]] > maxV:
                    maxV = Vol[arr[i][j]] + Vol[arr[i+di][j+dj]]
print(maxV)