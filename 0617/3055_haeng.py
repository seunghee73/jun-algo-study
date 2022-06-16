from collections import deque
D = [(1,0), (-1,0), (0,1), (0,-1)]

def spread(x,y):
    for i in D:
        X = x + i[0]
        Y = y + i[1]
        if 0<=X<C and 0<=Y<R and MAP[Y][X] == '.':
            MAP[Y][X] = '*'
            water.append((X,Y))

def BFS(s1,s2,c):
    global result
    for i in D:
        X = s1 + i[0]
        Y = s2 + i[1]
        if 0<=X<C and 0<=Y<R and not visited[Y][X] and (MAP[Y][X] =='.' or MAP[Y][X]=='D'):
            if (X,Y) == target:
                result = c+1
                return
            visited[Y][X] = 1
            location.append((X,Y,c+1))




R,C = map(int,input().split())
MAP =[]
water = deque()
location = deque()
for i in range(R):
    A = input()
    for j in range(C):
        if A[j] == 'D':
            target = (j,i)
        elif A[j] == 'S':
            location.append((j,i,0))
        elif A[j] == '*':
            water.append((j,i))
    MAP.append(list(A))

visited = [[0]*C for _ in range(R)]
result = 0

while location:
    n=len(water)
    while n>0:
        w1,w2 = water.popleft()
        spread(w1,w2)
        n -=1

    n2 = len(location)
    while n2>0:
        s1,s2,c = location.popleft()
        BFS(s1,s2,c)
        n2 -=1

    if result:
        break

if result:
    print(result)
else:
    print('KAKTUS')



