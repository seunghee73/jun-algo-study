import sys
input = sys.stdin.readline
INF = sys.maxsize

def binary(S, E, P):
    global ans
    while S < E:
        if A[P] + A[S] + A[E] == 0:
            temp = [A[P], A[S], A[E]]
            temp.sort()
            print(*temp)
            exit(0)
        else:
            if abs(A[P] + A[S] + A[E]) < abs(sum(ans)):
                ans = [A[P], A[S], A[E]]
            if A[P] + A[S] + A[E] < 0:
                S += 1
            else:
                E -= 1

N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = [INF] * 3

for i in range(N-2):
    S = i+1
    E = N-1
    binary(S, E, i)

ans.sort()
print(*ans)

