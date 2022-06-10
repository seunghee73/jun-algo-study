import re

T = int(input())
for t in range(T):
    N = input()
    result = re.compile('(100+1+|01)+').fullmatch(N)
    if result:
        print('YES')
    else:
        print('NO')