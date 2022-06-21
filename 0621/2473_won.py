import sys
input = sys.stdin.readline
# from collections import deque

N = int(input())
ARR = list(map(int, input().split()))
ARR.sort()
# print(ARR)
ans = []
minV = 9999999999999

def f():
    global ans, minV
    for i in range(N - 2):
        l = i + 1
        r = N - 1
        while l < r:
            tmp = ARR[i] + ARR[l] + ARR[r]
            if minV > abs(tmp):
                minV = abs(tmp)
                ans = [ARR[i], ARR[l], ARR[r]]
            if tmp > 0:
                r -= 1
            elif tmp < 0:
                l += 1
            elif tmp == 0:
                return
f()
print(*ans)
