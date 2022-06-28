import sys
input = sys.stdin.readline
# from collections import deque


T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        S = input().rstrip()
        arr.append(S)
    arr.sort()
    # print(arr)
    ans = 'YES'
    for i in range(N - 1):
        length = len(arr[i])
        if arr[i] == arr[i + 1][:length]:
            ans = 'NO'
            break
    print(ans)
