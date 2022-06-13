def find(x):
    ST = [x]
    visited = [[0]*C for _ in range(R)]
    while ST:
        now = ST.pop(0)
        for i in range(1,10):
            X = now[0] + D[str(i)][0]
            Y = now[1] + D[str(i)][1]
            if 0<=X<C and 0<=Y<R and visited[Y][X] == 0:
                ST.append((X,Y))
                visited[Y][X] = 1
                if MAP[Y][X] == 'R':
                    move(X,Y)



def move(x,y):
    MAP[y][x] = '.'
    short = (x,y)
    for j in range(1, 10):
        if abs(I[0] - (x + D[str(j)][0])) + abs(I[1] - (y + D[str(j)][1])) < abs(
                I[0] - short[0]) + abs(I[1] - short[1]):
            short = (x + D[str(j)][0], y + D[str(j)][1])

    if MAP[short[1]][short[0]] == 'I':
        print('kraj',N+1)
        exit()
    if MAP[short[1]][short[0]] == 'R':
        ST_R.append(short)

    MAP[short[1]][short[0]] = 'R'




R,C = map(int,input().split())
MAP = []

for i in range(R):
    A = list(input())
    if 'I' in A:
        I = (A.index('I'),i)
    MAP.append(A)
D = { '1':(-1,1),'2':(0,1), '3':(1,1), '4':(-1,0), '5':(0,0), '6':(1,0), '7':(-1,-1),'8':(0,-1),'9':(1,-1)}

NEXT = list(input())


for N in range(len(NEXT)):
    MAP[I[1]][I[0]] = '.'
    I = (I[0]+D[NEXT[N]][0], I[1]+D[NEXT[N]][1])
    if MAP[I[1]][I[0]] == 'R':
        print('kraj', N + 1)
        exit()
    MAP[I[1]][I[0]] = 'I'
    ST_R = []
    find(I)

    for k in ST_R:
        MAP[k[1]][k[0]] = '.'

for k in MAP:
    print("".join(k))



