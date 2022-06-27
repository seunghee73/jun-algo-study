t = int(input())
for _ in range(t):
    s = list(input())
    ls = len(s)
    ans = s
    i = ls-2
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1
    if i == -1:
        print(''.join(ans))
    else:
        j = ls-1
        while s[i] >= s[j]:
            j -= 1
        s[i], s[j] = s[j], s[i]
        ans = s[:i+1]
        ans.extend(list(reversed(s[i+1:])))
        print(''.join(ans))