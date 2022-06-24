import sys
sys.setrecursionlimit(10**9)

def func(a, b, e):
    global ans
    if ans:
        return
    if e == len(E):
        ans = True
    if a < len(A) and A[a] == E[e]:
        func(a+1, b, e+1)
    if b < len(B) and B[b] == E[e]:
        func(a, b+1, e+1)

N = int(input())
for n in range(1, N+1):
    A, B, E = list(map(str, input().split()))
    DP = [0] * len(E)
    ans = False

    for i in set(E):
        if i not in A and i not in B:
            ans = True
            break

    if ans:
        print('Data set %d: no'%n)
        continue

    DP = [0] * len(E)
    func(0, 0, 0)
    if ans:
        print('Data set %d: yes'%n)
    else:
        print('Data set %d: no'%n)