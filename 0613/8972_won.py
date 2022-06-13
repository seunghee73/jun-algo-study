import sys
input = sys.stdin.readline

dy = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dx = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

R, C = map(int, input().split())

G = [list(input().rstrip()) for _ in range(R)]
# print(G)
S = input().rstrip()

dic = [0] * len(S)

for i in range(len(dic)):
    dic[i] = int(S[i])

jongCoord = [-1, -1]
crazyCoords = []
for i in range(R):
    for k in range(C):
        if G[i][k] == 'I':
            jongCoord = [i, k]
        elif G[i][k] == 'R':
            crazyCoords.append([i, k])

def jongA(d):
    global jongCoord
    y, x = jongCoord
    ny, nx = y + dy[d], x + dx[d]
    if G[ny][nx] == 'R':
        return False
    G[y][x] = '.'
    G[ny][nx] = 'I'
    jongCoord = [ny, nx]
    return True

def crazyA():
    global crazyCoords
    newCrazy = {}
    for y, x in crazyCoords:
        G[y][x] = '.'
        dist = 9999999999999
        minCoord = [-1, -1]
        for d in range(1, 10):
            if d == 5:
                continue
            ny, nx = y + dy[d], x + dx[d]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            tmp = abs(ny - jongCoord[0]) + abs(nx - jongCoord[1])
            if dist > tmp:
                dist = tmp
                minCoord = (ny, nx)
        # print(minCoord)
        if G[minCoord[0]][minCoord[1]] == 'I':
            return False

        if newCrazy.get(minCoord):
            newCrazy[minCoord] += 1
        else:
            newCrazy[minCoord] = 1

    crazyCoords = []
    for y, x in newCrazy.keys():
        if newCrazy[(y, x)] == 1:
            G[y][x] = 'R'
            crazyCoords.append([y, x])
    return True


cnt = 0
flag = True
for d in dic:
    cnt += 1
    if not jongA(d):
        print('kraj', cnt)
        flag = False
        break
    if not crazyA():
        print('kraj', cnt)
        flag = False
        break
if flag:
    for i in range(R):
        for k in range(C):
            print(G[i][k], end='')
        print()
