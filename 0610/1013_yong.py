# 정규표현식 문제
# 입력된 문자열 전체가 매치되는지 확인하기 위해 fullmatch를 사용

import re
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    val = input().rstrip('\n')
    c = re.compile('(100+1+|01)+')
    if c.fullmatch(val):
        print('YES')
    else:
        print('NO')