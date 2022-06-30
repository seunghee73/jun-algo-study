def per(s,e):
    if s == e:
        ans = ''
        sol = []
        for i in range(n):
            val = i+1
            sol.append(val)
            ans += str(val)
            if i != n-1:
                ans += p[i]
                sol.append(p[i])
        if eval(ans) == 0:
            for s in sol:
                if s == '':
                    print(' ', end = '')
                else:
                    print(s, end='')
            print()

    else:
        for i in range(3):
            p[s] = lst[i]
            per(s+1, n-1)
TC = int(input())
for _ in range(TC):
    n = int(input())
    lst = ['', '+', '-']
    p = [0]*(n-1)
    per(0,n-1)
    print()


