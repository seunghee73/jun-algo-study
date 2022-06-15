change = { 0:[(1,0),(-1,0),(0,1),(0,-1)],1: [(1,0),(0,1),(0,-1)], 2: [(1,0),(-1,0),(0,1)] ,4: [(-1,0),(0,1),(0,-1)],8: [(1,0),(-1,0),(0,-1)],
           3: [(1,0),(0,1)], 5: [(0,1),(0,-1)],9: [(1,0),(0,-1)],6: [(-1,0),(0,1)],
           10: [(1,0),(-1,0)], 12: [(-1,0),(0,-1)], 7: [(0,1)],11: [(1,0)],
           13: [(0,-1)], 14: [(-1,0)], 15: []
           }

def bfs(x,y,c):
    global cnt
    ST = [(x,y)]
    visited[y][x] = c
    while ST:
        nx,ny = ST.pop(0)
        cnt += 1
        for j in change[road[ny][nx]]:
            X = nx + j[0]
            Y = ny + j[1]
            if 0<=X<N and 0<=Y<M and not visited[Y][X]:
                ST.append((X,Y))
                visited[Y][X] = c

N,M = map(int, input().split())
road = []
for _ in range(M):
    road.append(list(map(int, input().split())))


visited = [[0]*N for _ in range(M)]
result1 = 1
result2 = 0
room = [0]
for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            cnt = 0
            bfs(x,y,result1)
            result1 += 1
            room.append(cnt)
            if cnt > result2:
                result2 = cnt

result3=0
for y in range(M):
    for x in range(N):
        if x<N-1 and visited[y][x] != visited[y][x+1]:
            S = room[visited[y][x]]+room[visited[y][x+1]]
            if S>result3:
                result3 = S

        if y <M-1 and visited[y][x] != visited[y+1][x]:
            S = room[visited[y][x]]+room[visited[y+1][x]]
            if S>result3:
                result3 = S

print(result1-1)
print(result2)
print(result3)
