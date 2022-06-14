#220611 16500 문자열 판별
# make S to use word of A
# length of array A = N, N ~ 100
# length of string S = 100
# A의 문자열은 여러번 사용이 가능하다
# len(S)*len(A) = 100**2
# dp와 백트래킹
import sys
input = sys.stdin.readline

def backtrack(idx):
    global answer, S, N, A
    if idx == len(S):
        answer = 1
        return
    if dp[idx]:
        return
    dp[idx] = 1

    for aIdx in range(len(A)):
        aLen = len(A[aIdx])
        if len(S[idx:]) >= aLen:
            if S[idx:idx+aLen] == A[aIdx]:
                backtrack(idx+aLen)
    return

S = input().rstrip()
N = int(input())
A = []
for _ in range(N):
    a = input().rstrip()
    A.append(a)
dp = [0]*101
answer = 0
backtrack(0)
print(answer)
