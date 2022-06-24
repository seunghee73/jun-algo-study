import sys
input = sys.stdin.readline
from collections import deque

def f(arr):
    A, B, C = arr
    qu = deque()
    qu.append([-1, -1, -1])
    visited = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    while qu:
        ai, bi, ci = qu.popleft()
        if ai == len(A) - 1 and bi == len(B) - 1 and ci == len(C) - 1:
            return True
        elif ci == len(C) - 1:
            return False

        if ai + 1 < len(A) and ci + 1 < len(C) and A[ai + 1] == C[ci + 1] and visited[ai + 1][bi] == 0:
            visited[ai + 1][bi] = 1
            qu.append([ai + 1, bi, ci + 1])
        if bi + 1 < len(B) and ci + 1 < len(C) and B[bi + 1] == C[ci + 1] and visited[ai][bi + 1] == 0:
            visited[ai][bi + 1] = 1
            qu.append([ai, bi + 1, ci + 1])
    return False

T = int(input())
for tc in range(1, T + 1):
    ARR = list(input().split())
    # print(ARR)
    print(f'Data set {tc}: ', end='')
    if f(ARR):
        print('yes')
    else:
        print('no')
