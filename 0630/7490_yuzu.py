def dfs(depth, s):
    if depth == n+1:
        ss = s.replace(' ', '')
        if eval(ss) == 0:
            print(s)
        return
    dfs(depth + 1, s + ' ' + str(depth))
    dfs(depth + 1, s + '+' + str(depth))
    dfs(depth + 1, s + '-' + str(depth))

t = int(input())
for _ in range(t):
    n = int(input())
    dfs(2, '1')
    print()