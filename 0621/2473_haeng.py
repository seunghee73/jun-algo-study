N = int(input())

ink = list(map(int,input().split()))
ink.sort()


Y = 3000000001
ST=[]
for i in range(1,N-1):
    S = 0
    E = N - 1
    while S<i and E>i:
        y = ink[S] + ink[E]+ink[i]
        if abs(Y) > abs(y):
            Y = y
            ST = [ink[S],ink[i],ink[E]]
        if y > 0:
            E -= 1
        elif y < 0:
            S += 1
        else:
            print(*ST)
            exit()
print(*ST)