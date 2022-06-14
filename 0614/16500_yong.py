# DP문제
# 구현자체는 단순하지만 중복문자열 발생 시 시간초과를 해결하기 위해 DP를 적용
# 탐색 시작점에 방문표시를 해 중복적인 체크가 발생하지 않도록 한다.

import sys
input = sys.stdin.readline

def find(idx):
    if idx == len(S):
        return True
    if DP[idx]:
        return False
    DP[idx] = 1
    for i in arr:
        if S[idx:idx + len(i)] == i:
            if find(idx + len(i)):
                return True
    return False


S = input().rstrip('\n')
A = int(input())
arr = []
DP = [0] * len(S)
for _ in range(A):
    arr.append(input().rstrip('\n'))
for i in arr:
    if S[:len(i)] == i:
        if find(len(i)):
            print(1)
            exit()
print(0)