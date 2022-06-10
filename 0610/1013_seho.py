#2206010 1013 Contact
# 정규표헌식 문제
import re
import sys
input = sys.stdin.readline

n = int(input())
testStr = re.compile('(100+1+|01)+')
for _ in range(n):
    getStr = input()[:-1]
    if testStr.fullmatch(getStr):
        print("YES")
    else:
        print("NO")