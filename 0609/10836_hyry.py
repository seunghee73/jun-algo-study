import sys
input = sys.stdin.readline

M, N = map(int, input().split())
growth = [1] * (2 * M - 1)
for _ in range(N):
    zero, one, two = map(int, input().split())
    for i in range(zero, 2 * M - 1):
        if i < zero + one:
            growth[i] += 1
        else:
            growth[i] += 2

ans = growth[M:]
for row in range(M - 1, -1, -1):
    print(growth[row], *ans)