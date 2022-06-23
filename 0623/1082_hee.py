max_length = 50

N = int(input())
P = list(map(int, input().split()))
M = int(input())

DP = [-1] * (max_length+1)
ans = 0

for i in range(N):
    cost = P[i]
    DP[cost] = str(i)
    if cost <= M:
        ans = max(ans, i)

for i in range(M+1):
    for j in range(N-1,-1, -1):
        cost = P[j]

        if 0 <= i-cost and DP[i-cost] != -1:
            present_max = int(DP[i])
            front_add = int(str(j) + DP[i-cost])
            back_add = int(DP[i-cost]+str(j))

            DP[i] = str(max(present_max, front_add, back_add))
            ans = max(ans, int(DP[i]))
print(ans)