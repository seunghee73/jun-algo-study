import sys
input = sys.stdin.readline
# from collections import deque

T = int(input())
for _ in range(T):
    arr = list(input().rstrip())

    p1 = 0
    p2 = 1

    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i] and p1 < i:
            p1 = i

    for i in range(1, len(arr)):
        if arr[p1 - 1] < arr[i] and p2 < i:
            p2 = i

    if p1 != 0 and p2 != 0:
        arr[p1 - 1], arr[p2] = arr[p2], arr[p1 - 1]
        arr[p1:] = list(reversed(arr[p1:]))
    print(''.join(arr))

