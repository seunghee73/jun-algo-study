def find(X,sum,level,post):
    if level == N:
        if sum == 0:
            print(X)
        return
    if post >0:
        A = sum-post+(post*10+level+1)
        find(X+' '+str(level+1),A,level+1,post*10+(level+1))
    else:
        A = sum-post+(post*10-(level+1))
        find(X+' '+str(level+1),A,level+1,post*10-(level+1))
    find(X+'+'+str(level+1),sum+(level+1),level+1,+(level+1))
    find(X+'-'+str(level+1),sum-(level+1),level+1,-(level+1))

T = int(input())
for t in range(T):
    if t != 0:
        print()
    N =int(input())
    Nlist= [ i for i in range(1,N+1)]
    find('1',1,1,1)

