import sys
input = sys.stdin.readline
# from collections import deque

N = int(input())  # 3
P = list(map(int, input().split()))  # 6 7 8
M = int(input())  # 21

dp = [-1 for _ in range(M + 1)]

for number in range(N - 1, -1, -1):  # 2 1 0
    price = P[number]  # 8 7 6
    for k in range(price, M + 1):  # 8~21 7~21 6~21
        dp[k] = max(dp[k], dp[k - price] * 10 + number, number)

print(dp[M])
