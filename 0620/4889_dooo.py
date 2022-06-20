tc = 0
while True:
    tc+= 1
    lst = list(input())
    if '-' in lst:
        break
    st = []
    cnt = 0
    for i in lst:
        if len(st) == 0:
            if i == '}':
                i = '{'
                cnt += 1
            st.append(i)
        else:
            if i == '}':
                if st[-1] == '{':
                    st.pop()
            else:
                st.append(i)
    cnt += len(st)//2
    print('{}. {}'.format(tc, cnt))