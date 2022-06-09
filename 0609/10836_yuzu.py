import sys
input = sys.stdin.readline

m, n = map(int, input().split())
grow = [0]*(2*m-1)
for i in range(n):
    a, b, c = map(int, input(). split())
    for j in range(a, a+b):
        grow[j] += 1
    for j in range(a+b, a+b+c):
        grow[j] += 2

larva = [[1]*m for _ in range(m)]

side = []
for i in range(m-1, -1, -1):
    side.append((i, 0))
for i in range(1, m):
    side.append((0, i))

grow2 = [[0]*m for _ in range(m)]
for i in range(2*m-1):
    a, b = side[i]
    larva[a][b] += grow[i]
    grow2[a][b] = grow[i]
for x in range(1, m):
    for y in range(1, m):
        t = 0
        for dx, dy in [(0, -1), (-1, -1), (-1, 0)]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<m and 0<=ny<m and grow2[nx][ny] > t:
                t = grow2[nx][ny]
        larva[x][y] += t
        grow2[x][y] = t

for i in range(m):
    print(*larva[i])