t = int(input())
for tc in range(1, t+1):
    x = input().split()
    a = list(x[0])
    b = list(x[1])
    s = list(x[2])
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    dp[0][0] = 1
    for i in range(1, len(a)+1):
        if a[i-1] == s[i-1]:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = 0
    for i in range(1, len(b)+1):
        if b[i-1] == s[i-1]:
            dp[0][i] = dp[0][i-1]
        else:
            dp[0][i] = 0
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            ax = a[i-1]
            bx = b[j-1]
            sx = s[i+j-1]
            if ax != sx and bx != sx:
                dp[i][j] = 0
            elif ax == sx and bx != sx:
                dp[i][j] = dp[i-1][j]
            elif ax != sx and bx == sx:
                dp[i][j] = dp[i][j-1]
            else:
                if dp[i-1][j] or dp[i][j-1]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
    if dp[-1][-1] == 1:
        ans = 'yes'
    else:
        ans = 'no'
    print(f'Data set {tc}:', ans)