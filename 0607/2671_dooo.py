import re
val = input()
code = re.compile('(100+1+|01)+')
ans = code.fullmatch(val)
if ans:
    print("SUBMARINE")
else:
    print("NOISE")
