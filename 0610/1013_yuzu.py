import re

t = int(input())
for _ in range(t):
    s = input()
    if re.compile('(100+1+|01)+').fullmatch(s):
        print("YES")
    else:
        print("NO")