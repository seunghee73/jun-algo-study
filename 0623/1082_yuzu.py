n = int(input())
p = list(map(int, input().split()))
m = int(input())
lst = []
for i in range(n-1, -1, -1):
    lst.append((i, p[i]))
dp = ['0' for _ in range(m+1)]
for x, y in lst:
    for j in range(y, m+1):
        dp[j] = str(max((int(str(dp[j-y])+str(x))), int(str(x)), int(str(dp[j]))))
print(0) if dp[-1][0] == '0' else print(dp[-1])