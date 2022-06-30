def bfs():
    while Q:
        curV = Q.pop(0)
        if curV[-1] == f'{N}':
            if eval(curV) == 0:
                ans.append(curV)
            continue

        for oprtr in ('+', '-'):
            tmpNum = ''
            for num in range(int(curV[-1]) + 1, N + 1):
                tmpNum += str(num)
                Q.append(curV + oprtr + tmpNum)


T = int(input())
for _ in range(T):

    N = int(input())

    Q, num = [], ''
    for i in range(1, N + 1):
        num += str(i)
        Q.append(num)

    ans = []
    bfs()

    newAns = []
    for strV in ans:
        tmpStr = ' '
        for s in strV:
            if tmpStr[-1].isdigit() and s.isdigit():
                tmpStr += ' ' + s
            else:
                tmpStr += s
        newAns.append(tmpStr.lstrip())

    newAns.sort()
    for a in newAns:
        print(a)
    print()