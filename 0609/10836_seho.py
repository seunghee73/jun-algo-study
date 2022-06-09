#220609 10836 여왕벌
# 0,0 ~ (r-1, c-1)
# 칸에 있는 애벌레는 0 1 2 만큼 성장
# m < 700, n < 백만
import sys
input = sys.stdin.readline

m, n = map(int,input().split())
border =[1]*(2*m-1)

for _ in range(n):
    getGrow = list(map(int,input().split())) # 왼쪽아래(m-1,0)에서 왼쪽위(0,0)오른쪽위(0,m-1)까지
    # 0, 1, 2 들의 개수를 입력. 총개수는 2m-1개임이 자명.
    for idx in range(getGrow[0],getGrow[0]+getGrow[1]):
        border[idx] += 1
    for idx in range(getGrow[0]+getGrow[1],getGrow[0]+getGrow[1]+getGrow[2]):
        border[idx] += 2

for r in range(m):
    for c in range(m):
        if c == 0:
            print(border[m-1-r], end = " ")
        else:
            print(border[m+c-1], end = " ")
    print()
