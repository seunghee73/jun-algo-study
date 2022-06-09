import sys
input = sys.stdin.readline

M, N = map(int, input().split())
temp = [1] * (2 * M - 1)
for _ in range(N):
    zero, one, two = list(map(int, input().split()))

    for i in range(zero, zero + one):
        temp[i] += 1
    for i in range(zero + one, zero + one + two):
        temp[i] += 2

col = temp[:M]
row = temp[M:]

for y in range(M-1, -1, -1):
    A = [col[y]] + row
    print(*A)