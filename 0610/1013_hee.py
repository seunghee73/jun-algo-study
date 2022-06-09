import re
N = int(input())
P = re.compile('(100+1+|01)+')
for _ in range(N):
    A = P.fullmatch(input())
    if A:
        print('YES')
    else:
        print('NO')