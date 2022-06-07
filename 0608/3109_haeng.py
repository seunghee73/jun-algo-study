def pipe(X,Y):
    global c,result

    if X == C - 1:
        for vX,vY in ST:
            road[vY][vX] = '@'
        result += 1
        c=1
        return

    if 0 <= Y-1 and road[Y-1][X+1] == '.':
        ST.append((X+1, Y-1))
        pipe(X+1,Y-1)
        if c:
            return
        else:
            ST.pop()

    if road[Y][X+1] == '.':
        ST.append((X+1, Y))
        pipe(X+1, Y)
        if c:
            return
        else:
            ST.pop()

    if Y+1 < R and road[Y+1][X+1] == '.':
        ST.append((X+1, Y+1))
        pipe(X+1,Y+1)
        if c:
            return
        else:
            ST.pop()

    road[Y][X] = '@'
    return

R,C = map(int,input().split())
road = []
for _ in range(R):
    road.append(list(input()))

result=0
for i in range(R):
    ST = []
    c=0
    pipe(0,i)

print(result)