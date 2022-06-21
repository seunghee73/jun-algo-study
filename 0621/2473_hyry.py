# 백트래킹은 무조건 시초...

def solution():
    global minLst, minV

    for start in range(N - 2):
        left = start + 1
        right = N - 1

        while left < right:
            tmp = arr[start] + arr[left] + arr[right]

            if abs(tmp) < abs(minV):
                minV = tmp
                minLst = [arr[start], arr[left], arr[right]]

            if tmp == 0:
                minLst = [arr[start], arr[left], arr[right]]
                return
            if tmp > 0:
                right -= 1
            if tmp < 0:
                left += 1


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
minV = 1e10
minLst = [1e10, 1e10, 1e10]
solution()
print(*minLst)