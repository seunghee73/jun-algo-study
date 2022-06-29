#220630 7490 0 만들기
# 1 ~ N 의 값을 갖는 수열이 있다고 할때,
# 각 숫자 사이마다 + - 공백을 삽입
# eval 했을때 0이 되는 수식을 출력하라
# + - 공백을 반복하는 백트래킹?

import sys

input = sys.stdin.readline

def backtrack(calcLoc):
    global visited, calc,result, num, lst

    if calcLoc == num-1:
        answer = lst[0]
        for idx in range(num-1):
            answer += result[idx]
            answer += lst[idx+1]
        if eval(answer.replace(" ","")) == 0:
            print(answer)
        return

    for nxtCalc in calc:
        result[calcLoc] = nxtCalc
        backtrack(calcLoc+1)
tc_num = int(input())

for tc in range(tc_num):
    num = int(input())

    lst = [str(i) for i in range(1,num+1)]
    visited = [0]*(num)
    result = [-1 for _ in range(num-1)]
    calc = [" ","+","-"]
    backtrack(0)

    print()