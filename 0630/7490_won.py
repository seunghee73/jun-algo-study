import sys
input = sys.stdin.readline
from collections import deque

def isZero(form):
    front = 0
    back = ''
    op = '+'
    for i in range(len(form)):
        if form[i].isdigit():
            back += form[i]
        else:
            if form[i] == '+':
                if op == '+':
                    front += int(back)
                    back = ''
                elif op == '-':
                    front -= int(back)
                    back = ''
                op = '+'
            elif form[i] == '-':
                if op == '+':
                    front += int(back)
                    back = ''
                elif op == '-':
                    front -= int(back)
                    back = ''
                op = '-'

    if op == '' or op == '+':
        front += int(back)
    else:
        front -= int(back)
    # print(form, front)
    if front == 0:
        return True
    return False

def f(dep, form):
    global ans
    if dep == N:
        # print(form)
        if isZero(form):
            ans.append(form)
        return
    # 더하기
    f(dep + 1, form + '+' + str(dep + 1))
    # 빼기
    f(dep + 1, form + '-' + str(dep + 1))
    # 공백
    f(dep + 1, form + ' ' + str(dep + 1))

T = int(input())
for _ in range(T):
    N = int(input())
    ans = []
    f(1, '1')
    ans.sort()
    for i in ans:
        print(i)
    print()
