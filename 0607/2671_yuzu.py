import re

s = input()
if re.compile('(100+1+|01)+').fullmatch(s):
    print("SUBMARINE")
else:
    print("NOISE")