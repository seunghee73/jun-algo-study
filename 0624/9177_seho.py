# 2206024 9177 단어 섞기
# 주어진 두개 단어의 각 순서를 유지하여 배치할 수 있을때,
# 세번째 단어를 만들수 있는가?
# a, b => c. a와 b의 길이는 200
# 1000의 테스트케이스 주어짐
# c의 길이만큼 리스트 생성
# 이차원을 활용한 우선탐색 or dp


import sys

input = sys.stdin.readline
from collections import deque

n = int(input())

for tc in range(1,n+1):
    A, B, C = input()[:-1].split()
    result = 'no'
    visited = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]
    cIdx = 0

    queue = deque([[0,0]])

    while queue:
        for _ in range(len(queue)):
            a, b = queue.popleft()
            if a < len(A) and visited[a+1][b] == -1 and A[a] == C[cIdx]:
                visited[a+1][b] = 1
                queue.append([a+1,b])
            if b < len(B) and visited[a][b+1] == -1 and B[b] == C[cIdx]:
                visited[a][b+1] = 1
                queue.append([a,b+1])
        cIdx += 1
    if cIdx == len(C)+1:
        result = 'yes'
    print("Data set {0}: {1}".format(tc, result))


