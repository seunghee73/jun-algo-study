def find(x,L):
    global s
    ST = [[] for _ in range(10)]
    for k in L:
        long = len(k)
        if long == x:
            s = 1
            return
        else:
            ST[int(k[x])].append(k)
    for j in ST:
        if len(j) > 1:
            find(x+1,j)
            if s:
                return

T = int(input())
for t in range(T):
    N = int(input())

    tel = [[] for _ in range(10)]


    for _ in range(N):
        a = input()
        tel[int(a[0])].append(a)

    s = 0
    for i in tel:
        if len(i)>1:
            find(1,i)

    if s:
        print('NO')
    else:
        print('YES')