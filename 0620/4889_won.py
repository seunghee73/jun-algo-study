import sys
input = sys.stdin.readline
# from collections import deque

cnt = 0
while True:
    S = input().rstrip()
    cnt += 1
    if S[0] == '-':
        break
    ans = 0

    st = []
    for i in range(len(S)):
        if S[i] == '{':
            st.append(S[i])
        else:
            if st:
                if st[-1] == '{':
                    st.pop()
                else:
                    st.append(S[i])
            else:
                st.append(S[i])
    # print(st)
    k = 1
    while k < len(st):
        if st[k - 1] == '{' and st[k] == '{':
            ans += 1
            k += 1
        elif st[k - 1] == '}' and st[k] == '{':
            ans += 2
            k += 1
        elif st[k - 1] == '}' and st[k] == '}':
            ans += 1
            k += 1
        k += 1
    print(f'{cnt}. {ans}')
