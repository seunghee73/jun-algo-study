def check(X):
    ST =[X[0]]
    visited =[0]*7
    visited[0] = 1
    while ST:
        nx,ny =ST.pop()
        for i,j in (1,0),(-1,0),(0,1),(0,-1):
            nX = nx + i
            nY = ny + j
            if (nX,nY) in X and visited[X.index((nX,nY))] ==0:
                ST.append((nX,nY))
                visited[X.index((nX,nY))] = 1
    if visited == [1]*7:
        return 1

def find(level,i,S,Y):
    global result
    if level ==7 and check(G7) and S>=4:
        result +=1
        return
    if level >= 4 and 7 - level + S < 4:
        return
    for j in range(i+1,25):
        G7.append((A[j][0],A[j][1]))
        if A[j][2] == 'S':
            find(level+1, j, S+1, Y)
        else:
            find(level+1, j, S, Y+1)
        G7.pop()

G = []
for _ in range(5):
    G.append(input())

result = 0
A = []
for y in range(5):
    for x in range(5):
        A.append((x,y,G[y][x]))
G7=[]
for i in range(25):
    G7.append((A[i][0],A[i][1]))
    if A[i][2] == 'S':
        find(1,i,1,0)
    else:
        find(1,i,0,1)
    G7.pop()


print(result)