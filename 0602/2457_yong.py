import sys
input = sys.stdin.readline

# dfs로 풀려한 흔적, 자료가 너무 많아서 시초엔딩
# def dfs(sM, sD, eM, eD, cnt):
#     global ans
#     if ans <= cnt:
#         return
#     for i in range(N):
#         if not visited[i]:
#             newsM, newsD, neweM, neweD = arr[i]
#             if (newsM == eM and newsD <= eD) or (newsM < eM):
#                 visited[i] = 1
#                 if neweM > 11:
#                     if ans > cnt+1:
#                         ans = cnt+1
#                     visited[i] = 0
#                     return
#                 else:
#                     dfs(newsM, newsD, neweM, neweD, cnt+1)
#                     visited[i] = 0

# 날짜를 하나의 숫자로 바꾼 뒤 비교를 통해 판단
# 조건에 맞다면 cnt를 아니라면 0을 출력
N = int(input())
arr = []
for _ in range(N):
    startM, startD, endM, endD = map(int, input().split())
    arr.append((100*startM + startD, 100*endM + endD))
startD = 301
endD = 1130
cnt = 0
while True:
    maxV = 0
    for i in arr:
        if i[0] <= startD and i[1] > startD:
            if i[1] > maxV:
                maxV = i[1]
    
    if maxV:
        cnt += 1
        startD = maxV
        if startD > endD:
            break
    else:
        break

if startD > endD:
    print(cnt)
else:
    print(0)