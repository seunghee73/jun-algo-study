import sys

r, c = map(int, input().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
game = list(input())

dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

player = []
arduino = set()
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'I':
            player.append((i, j))
        elif arr[i][j] == 'R':
            arduino.add((i, j))

def crazy_arduino(player, arduino):
    cnt = 0
    for p in game:
        cnt += 1
        p = int(p)
        x, y = player.pop(0)
        nx = x + dx[p]
        ny = y + dy[p]

        if (nx, ny) in arduino:
            print("kraj", cnt)
            return

        box1 = set()
        box2 = set()
        for ax, ay in arduino:
            min = 1e9
            mp = 0
            for i in (1, 2, 3, 4, 6, 7, 8, 9):
                dist = abs(ax+dx[i]-nx) + abs(ay+dy[i]-ny)
                if min > dist:
                    min = dist
                    mp = i

            if (ax+dx[mp], ay+dy[mp]) in box1:
                box2.add((ax+dx[mp], ay+dy[mp]))
            box1.add((ax+dx[mp], ay+dy[mp]))

            if min == 0:
                print("kraj", cnt)
                return

        arduino = box1-box2

        player.append((nx, ny))

    for i in range(r):
        for j in range(c):
            if (i, j) in arduino:
                print('R', end='')
            elif (i, j) in player:
                print('I', end='')
            else:
                print('.', end='')
        print()
    return

crazy_arduino(player, arduino)