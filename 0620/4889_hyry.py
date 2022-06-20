
import sys
input = sys.stdin.readline

num = 0
while True:
    strV = input().rstrip()
    num += 1
    if '-' in strV: break
    while '{}' in strV:
        strV = strV.replace('{}', "")

    ST = []
    ans = 0
    for s in strV:
        if not ST:
            ST.append(s)
        else:
            if (ST[-1], s) == ('}', '{'):
                tmp = ST.pop()
                ans += 2
            elif ST[-1] == s == '}':
                ST.pop()
                ans += 1
            elif (ST[-1], s) == ('{', '}'):
                tmp = ST.pop()
            elif ST[-1] == s == '{':
                ST.append(s)

    if ST:
        ans += len(ST) // 2

    print(f'{num}. {ans}')