s = input()
n = int(input())
dp = [0]*len(s) + [1]

a_box = []
for _ in range(n):
    a = input()
    a_box.append(a)

for i in range(len(s)-1, -1, -1):
    for a in a_box:
        if s[i:i+len(a)] == a and dp[i+len(a)] == 1:
            dp[i] = 1
print(dp[0])