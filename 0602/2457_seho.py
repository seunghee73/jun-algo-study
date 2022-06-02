#220602 2457 공주님의 정원
## n개의 꽃종류.. 0301 ~ 1130 까지 꽃 한가지 이상 피어있도록 유지
## n <= 100,000
## 가능한 적은 개수의 꽃 심을 것.

import sys
input = sys.stdin.readline

n = int(input())
flowers = []

## 0301 ~ 1130...
for _ in range(n):
    flowers.append(list(map(int,input().split())))
answer = 0
flowers.sort()

planStart = [3,1]
idx = 0
check = False
while idx <= len(flowers):

    candidates = []
    for nxtIdx in range(idx,len(flowers)):
        startDate = flowers[nxtIdx][0:2]
        endDate = flowers[nxtIdx][2:]
        if startDate[0] < planStart[0] or (startDate[0] == planStart[0] and startDate[1] <= planStart[1]):
            ent = flowers[nxtIdx].copy()
            ent.append(nxtIdx)
            candidates.append(ent)
    if candidates:
        candidates.sort(key=lambda x: x[2:4])
        idx = candidates[-1][-1]
        planStart = flowers[idx][2:]
        idx += 1
        answer += 1
    else:
        break
    if planStart[0] > 11 or (planStart[0] == 11 and planStart[1] >= 31):
        check = True
        break
if check:
    print(answer)
else:
    print(0)