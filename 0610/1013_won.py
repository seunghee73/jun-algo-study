import sys
import re
input = sys.stdin.readline

T = int(input())
for _ in range(1, T + 1):
    S = input().rstrip()

    ans = re.compile('(100+1+|01)+').fullmatch(S)

    if ans:
        print('YES')
    else:
        print('NO')
