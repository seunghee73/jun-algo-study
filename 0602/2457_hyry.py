import sys
input = sys.stdin.readline


def howMany():

    tmpM = tmpD = 0
    for sM, sD, eM, eD in flowers:
        if sM < startMonth:
            if eM > tmpM:
                tmpM, tmpD = eM, eD
            elif eM == tmpM and eD > tmpD:
                tmpM, tmpD = eM, eD
        if sM == startMonth:
            if sD <= startDay:
                if eM > tmpM:
                    tmpM, tmpD = eM, eD
                elif eM == tmpM and eD > tmpD:
                    tmpM, tmpD = eM, eD

    return tmpM, tmpD



N = int(input())
flowers = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    flowers.append([a, b, c, d])
flowers.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]))
startMonth, startDay = 3, 1
endMonth, endDay = 11, 30
cnt = 0

while True:
    tmpM, tmpD = howMany()

    if tmpM == tmpD == 0:
        cnt = 0
        break

    if startMonth == tmpM and startDay == tmpD:
        cnt = 0
        break

    if tmpM and tmpD:
        cnt += 1
        startMonth, startDay = tmpM, tmpD

    if startMonth == 12:
        break

print(cnt)