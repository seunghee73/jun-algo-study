import sys

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
min_val = min(lst)
inf = sys.maxsize
dp = [-inf] *(m+1)
for i in range(n-1, -1, -1):
    p = lst[i]
    for j in range(p, m+1):
        dp[j] = max(dp[j-p]*10+i, i, dp[j])
print(dp[m])