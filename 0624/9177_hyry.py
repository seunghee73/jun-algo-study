import sys
from collections import deque
input = sys.stdin.readline


def mixing():
    Q = deque([(0, 0, 0)])
    visit = {(0, 0, 0)}

    while Q:
        first, second, depth = Q.popleft()
        if first == A and second == B:
            return 'yes'

        neiFirst = first + 1
        neiSecond = second + 1

        if neiFirst <= A and a[neiFirst - 1] == c[depth] and (neiFirst, second, depth + 1) not in visit:
            Q.append((neiFirst, second, depth + 1))
            visit.add((neiFirst, second, depth + 1))

        if neiSecond <= B and b[neiSecond - 1] == c[depth] and (first, neiSecond, depth + 1) not in visit:
            Q.append((first, neiSecond, depth + 1))
            visit.add((first, neiSecond, depth + 1))

    return 'no'


T = int(input())

for t in range(1, T + 1):

    a, b, c = input().split()
    A, B, C = len(a), len(b), len(c)

    ans = mixing()
    print(f'Data set {t}: {ans}')

'''
1
aaaaa baaaa baaaaaaaaa
'''