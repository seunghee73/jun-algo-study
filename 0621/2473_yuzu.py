n = int(input())
lst = list(map(int, input().split()))
lst.sort()

def twoPoint():
    ans = [0, 0, 0]
    res = 1e10
    for i in range(n-2):
        l = i+1
        r = n-1
        while l<r:
            s = lst[l] + lst[r] + lst[i]
            if abs(s) < abs(res):
                res = s
                ans = [lst[l], lst[r], lst[i]]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                return ans
    return ans

ans = twoPoint()
ans.sort()
print(*ans)