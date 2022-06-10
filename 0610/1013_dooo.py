import re
tc = int(input())
for i in range(tc):
    code = input()
    ans = re.compile('(100+1+|01)+')
    if ans.fullmatch(code):
        print("YES")
    else:
        print("NO")