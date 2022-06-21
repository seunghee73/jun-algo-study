# 이분탐색 문제
# 먼저 하나의 값을 지정한 후 남은 값들을 활용해 이분탐색 진행
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
minV = 3000000000
ans = []

for i in range(N-2):
    j = i + 1
    k = N-1
    while j < k:
        if abs(lst[i] + lst[j] + lst[k]) < minV:
            minV = abs(lst[i] + lst[j] + lst[k])
            ans = [lst[i], lst[j], lst[k]]

        if lst[i] + lst[j] + lst[k] > 0:
            k -= 1
        elif lst[i] + lst[j] + lst[k] < 0:
            j += 1
        else:
            print(*ans)
            exit()
print(*ans)