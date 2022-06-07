import sys
input = sys.stdin.readline
import re

S = input().rstrip()

ans = re.compile('(100+1+|01)+').fullmatch(S)

if ans:
    print('SUBMARINE')
else:
    print('NOISE')
