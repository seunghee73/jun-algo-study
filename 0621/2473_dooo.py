import sys
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
min_val = sys.maxsize
ans = []
for i in range(n-2):
    start = i + 1
    end = n-1
    while start < end:
        sol = arr[i] + arr[start] + arr[end]
        if abs(sol) < min_val:
            min_val = abs(sol)
            ans = [arr[i], arr[start], arr[end]]
        if sol > 0:
            end -= 1
        elif sol < 0:
            start += 1
        elif sol == 0:
            break
print(*ans)