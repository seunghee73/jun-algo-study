t = 1
while True:
    A = list(input())
    if A.count('-') > 1:
        break

    ST = []
    for i in A:
        if ST and ST[-1] == '{' and i == '}':
            ST.pop()
        else:
            ST.append(i)

    cnt = 0
    for i in range(len(ST)):
        if not i % 2:
            if ST[i] != '{':
                cnt += 1

        else:
            if ST[i] != '}':
                cnt += 1
    print(f'%d.'%t, cnt)
    t += 1