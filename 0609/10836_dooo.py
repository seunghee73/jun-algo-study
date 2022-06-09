n, m = map(int, input().split())
arr = [[1] * n for _ in range(n)]
lst = [1] * (2*n- 1)
for i in range(m):
    zero, one, two = map(int, input().split())
    for i in range(zero, zero+one):
        lst[i] += 1
    for j in range(zero+one, zero + one + two):
        lst[j] += 2
for i in range(n):
    arr[-i-1][0] = lst[i]
for j in range(1, n):
    for i in range(n):
        arr[i][j] = lst[n+j-1]
for i in arr:
    print(*i)