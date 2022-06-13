import sys
input = sys.stdin.readline
INF = sys.maxsize

def three(ir, ic, jr, jc):
    temp = INF
    for d in D:
        if d[0] == 0 and d[1] == 0:
            continue
        nc = ic + d[0]
        nr = ir + d[1]
        if not (-1 < nc < C and -1 < nr < R):
            continue
        if abs(nc-jc) + abs(nr-jr) < temp:
            r, c = nr, nc
            temp = abs(nc-jc) + abs(nr-jr)
    return r, c

I = []
R, C = map(int, input().split())
for r in range(R):
    L = list(input())
    for c in range(C):
        if L[c] == 'I':
            J = (r, c)
        elif L[c] == 'R':
            I.append((r, c))

A = list(input().strip())
D = [(0, 0), (-1, 1), (0, 1), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

for t in range(len(A)):
    # step 1
    d = int(A[t])
    jr, jc = J[0] + D[d][1], J[1] + D[d][0]
    J = (jr, jc)

    # step 2
    for ir, ic in I:
        if ir == jr and ic == jc:
            print('kraj', t+1)
            exit(0)

    V = set()
    temp = set()
    for i in range(len(I)):
        ir, ic = I[i]

        # step 3
        ir, ic = three(ir, ic, jr, jc)

        if (ir, ic) in V:
            temp.add((ir, ic))
        else:
            V.add((ir, ic))

        # step 4
        if (ir, ic) == (jr, jc):
            print('kraj', t+1)
            exit(0)

    I = list(V-temp)

G = [['.'] * C for _ in range(R)]
G[J[0]][J[1]] = 'I'
for i in I:
    G[i[0]][i[1]] = 'R'

for i in G:
    print(''.join(i))


