import sys
input = sys.stdin.readline


D = {
    '1': (1, -1), '2': (1, 0), '3': (1, 1), '4': (0, -1), '5': (0, 0),
    '6': (0, 1), '7': (-1, -1), '8': (-1, 0), '9': (-1, 1)
}

R, C = map(int, input().rstrip().split())
MAP = [list(input().rstrip()) for _ in range(R)]
rounds = list(input().rstrip())

iR = iC = -1
robots = set()
for row in range(R):
    for col in range(C):
        if MAP[row][col] == 'I':
            iR, iC = row, col
        if MAP[row][col] == 'R':
            robots.add((row, col))


for idx, turn in enumerate(rounds):

    # 1. turn에 따라 종수 이동
    iR = iR + D[turn][0]
    iC = iC + D[turn][1]

    # 2. 이동한 곳에 아두이노가 있는 경우
    if (iR, iC) in robots:
        print(f'kraj {idx + 1}')
        break

    flag = False
    tmp = set()
    delete = set()
    # 3. 미친 아두이노들 이동
    for robotR, robotC in robots:
        minV = 1e10
        nextR = nextC = -1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            newR, newC = robotR + dr, robotC + dc
            if 0 <= newR < R and 0 <= newC < C:
                tmpMin = abs(iR - newR) + abs(iC - newC)
                if minV > tmpMin:
                    minV = tmpMin
                    nextR, nextC = newR, newC

        # 4. 아두이노가 간 자리에 종수 아두이노가 있는지 체크
        if (nextR, nextC) == (iR, iC):
            flag = True
            print(f'kraj {idx + 1}')
            break

        # 5. 미친 아두이노가 간 자리에 다른 아두이노가 있는지 체크
        if (nextR, nextC) in tmp:
            delete.add((nextR, nextC))
        else:
            tmp.add((nextR, nextC))

    if flag: break

    tmp = tmp - delete # set 차집합
    robots = tmp
# 6. turn을 다하고 끝난 경우
else:
    ans = [['.'] * C for _ in range(R)]
    for row in range(R):
        for col in range(C):
            if (row, col) == (iR, iC):
                ans[row][col] = 'I'
            if (row, col) in robots:
                ans[row][col] = 'R'

    for a in ans:
        print(''.join(a))