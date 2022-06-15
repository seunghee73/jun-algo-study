from collections import deque

D = [(1,0), (-1,0), (0,1), (0,-1)]

def spread(x,y):
    for i in D:
        X = x + i[0]
        Y = y + i[1]
        if 0<=X<w and 0<=Y<h and MAP[Y][X] != '#' and not visited_f[Y][X]:
            MAP[Y][X] = '*'
            ST_fire.append((X,Y))
            visited_f[Y][X] = 1

def BFS(s1,s2,c):
    global result
    for i in D:
        X = s1 + i[0]
        Y = s2 + i[1]
        if 0<=X<w and 0<=Y<h and not visited_s[Y][X] and MAP[Y][X] =='.':
            if X ==0 or X == w-1 or Y ==0 or Y == h-1:
                result = c+1
                return
            visited_s[Y][X] = 1
            SG.append((X,Y,c+1))


T = int(input())
for t in range(T):
    w,h = map(int, input().split())
    MAP = []
    ST_fire = deque()
    s=0
    visited_f = [[0]*w for i in range(h)]
    for i in range(h):
        A = input()
        for j in range(w):
            if A[j] == '@':
                if j == 0 or j == w-1 or i==0 or i==h-1:
                    s=1
                sang = (j,i)
            if A[j] == '*':
                ST_fire.append((j,i))
                visited_f[i][j] = 1
        MAP.append(list(A))
    if s:
        print(1)
        continue

    visited_s = [[0]*w for i in range(h)]
    visited_s[sang[1]][sang[0]]=1
    SG = deque()
    SG.append((sang[0],sang[1],0))
    result = 0


    while SG:
        n = len(ST_fire)
        while n > 0:
            f1,f2 = ST_fire.popleft()
            spread(f1, f2)
            n -= 1

        n2 = len(SG)
        while n2 > 0:
            s1,s2,c = SG.popleft()
            BFS(s1,s2,c)
            n2 -= 1

        if result or not SG:
            break

    if result:
        print(result+1)
    else:
        print('IMPOSSIBLE')