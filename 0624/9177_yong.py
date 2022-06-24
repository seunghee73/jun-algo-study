# bfs를 활용한 탐색 문제
# 문자열을 차례로 탐색하여 가능한 경우를 큐에 넣어 끝까지 탐색

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    lst = deque([[len(a), len(b), len(c)]])
    visited = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    while lst:
        A, B, C = lst.popleft()
        if A == B == C == 0:
            return True
        elif C == 0:
            return False
        
        if A > 0 and a[A-1] == c[C-1] and visited[A-1][B] == 0:
            visited[A-1][B] = 1
            lst.append([A-1, B, C-1])
        if B > 0 and b[B-1] == c[C-1] and visited[A][B-1] == 0:
            visited[A][B-1] = 1
            lst.append([A, B-1, C-1])
    else:
        return False
    

N = int(input())
for n in range(1, N+1):
    a, b, c = input().split()
    if bfs():
        print(f'Data set {n}: yes')
    else:
        print(f'Data set {n}: no')