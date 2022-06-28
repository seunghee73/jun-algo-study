t = int(input())
for _ in range(t):
    n = int(input())
    ns = []
    G = dict()

    for _ in range(n):
        P = G
        c = list(input())
        ns.append(c)

        for i in c:
            if i not in P:
                P[i] = dict()
            P = P[i]

    for i in ns:
        P = G
        for j in i:
            P = P[j]
        if P.items():
            print('NO')
            break
    else:
        print('YES')