from collections import deque

T = int(input())
for t in range(T):
    word1,word2,word3  = input().split()

    w1 = len(word1)
    w2 = len(word2)
    w3 = w1 + w2
    ST = deque()
    ST.append((0,0))
    visited =[[0]*(w2+1) for _ in range(w1+1)]
    result = 0
    while ST:
        nw1,nw2 = ST.popleft()
        if nw1 + nw2 == w3:
            result += 1
            break
        if nw1<w1 and word3[nw1+nw2] == word1[nw1] and not visited[nw1+1][nw2]:
            ST.append((nw1+1,nw2))
            visited[nw1+1][nw2]=1


        if nw2<w2 and word3[nw1+nw2] == word2[nw2] and not visited[nw1][nw2+1]:
            ST.append((nw1,nw2+1))
            visited[nw1][nw2+1]=1

    if result:
        print('Data set {}: yes'.format(t + 1))
    else:
        print('Data set {}: no'.format(t + 1))