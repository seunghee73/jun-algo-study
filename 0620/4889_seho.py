#220620 4889 안정적인 문자열
# 빈문자열은 안정/ S가 안정적이면 {s}도 안정/ S, T가 안정이면 ST{S와T의연걸된문자열} 도 안정
# 문자열이 닫히지 않으면 안정적이지 않다.
# 안정적인 문자열을 만들기 위한 최소연산의 수?
# 여기서 연산은 닫힌 괄호를 열린 괄호로 아니면 그 역 뿐이다.
# s가 계속 주어짐. len(s) < 2000

import sys
from collections import deque
input = sys.stdin.readline
tcNum = 0
while 1:
    tcNum += 1
    getStr = input().rstrip()
    if getStr[0] == "-":
        break
    result = deque()

    for s in getStr:
        result.append(s)
        if len(result) >= 2:
            if "".join([result[-2],result[-1]]) == "{}":
                result.pop()
                result.pop()
    answer = 0
    if result:
        output = []
        for r in result:
            if output:
                if r == "{":
                    answer += 1
                output = []
            else:
                if r == "}":
                    answer += 1
                output.append("{")
        print("{0}. {1}".format(tcNum,answer))
    else:
        print("{0}. {1}".format(tcNum,answer))
