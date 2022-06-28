# 백트래킹으로 구현하는 경우, python에서는 더 빠르고 pypy에서는 느리다.
def dfs(arr):
    ST = [arr[0]]
    V = [False] * 7
    V[0] = True
    while ST:
        x, y = ST.pop()
        for i in range(7):
            if V[i]:
                continue

            xx, yy = arr[i]
            for d in D:
                nx, ny = x + d[0], y + d[1]
                if nx == xx and ny == yy:
                    V[i] = True
                    ST.append((nx, ny))

    if V == [True]*7:
        return True

def func(idx, total, num):
    if total == 7:
        if 4 <= num:
            global ans
            if dfs(temp):
                ans += 1
        return

    if 7 - total < 4 - num:
        return

    for i in range(idx+1, 25):
        if G[i] == 'S':
            temp.append((i%5, i//5))
            func(i, total+1, num+1)
            temp.pop()
        else:
            temp.append((i%5, i//5))
            func(i, total+1, num)
            temp.pop()

G = []
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for y in range(5):
    L = list(input())
    G.extend(L)

ans = 0
for i in range(25):
    temp = [(i%5, i//5)]
    if G[i] == 'S':
        func(i, 1, 1)
    else:
        func(i, 1, 0)
print(ans)

# combinations 사용하는 경우, python에서는 더 느리고 pypy에서는 더 빠르다.
from itertools import combinations

def dfs(arr):
    ST = [arr[0]]
    V = [False] * 7
    V[0] = True
    while ST:
        x, y = ST.pop()
        for i in range(7):
            if V[i]:
                continue

            xx, yy = arr[i]
            for d in D:
                nx, ny = x + d[0], y + d[1]
                if nx == xx and ny == yy:
                    V[i] = True
                    ST.append((nx, ny))

    if V == [True]*7:
        return True

G = []
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
for y in range(5):
    L = list(input())
    G.extend(L)
for i in combinations(range(25), 7):
    temp = []
    num = 0
    for j in i:
        temp.append((j%5, j//5))
        if G[j] == 'S':
            num += 1
    if 4 <= num and dfs(temp):
        ans += 1
print(ans)


