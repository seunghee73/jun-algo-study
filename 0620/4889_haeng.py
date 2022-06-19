T = 1
while 1:
    A = input()
    result = 0

    if '-' in A:
        break
    ST = []
    for i in range(len(A)):
        if i == 0:
            ST.append(A[i])
        elif ST and A[i] == '}' and ST[-1] == '{':
            ST.pop()
        else:
            ST.append(A[i])
    while ST:
        if ST[-1] == '{' and ST[-2] == '{':
            result += 1
            ST.pop()
            ST.pop()
        elif ST[-1] == '}' and ST[-2] == '}':
            result += 1
            ST.pop()
            ST.pop()
        elif ST[-1] == '{' and ST[-2] == '}':
            result += 2
            ST.pop()
            ST.pop()
    print('{}. {}'.format(T,result))
    T += 1