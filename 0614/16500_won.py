import sys
input = sys.stdin.readline

S = input().rstrip()

cand = []
for _ in range(int(input())):
    cand.append(input().rstrip())

dp = [0] * (len(S))
ans = 0
n = len(S)

def f(idx):
    global ans
    if idx == n:
        ans = 1
        return

    if dp[idx] == 1:
        return

    dp[idx] = 1

    for word in cand:
        m = len(word)
        if m <= n - idx:
            for k in range(m):
                if word[k] != S[idx + k]:
                    break
            else:
                f(idx + len(word))

f(0)
print(ans)
