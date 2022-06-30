# 조건에 맞는 계산식을 구해 출력하는 문제
# ASC순서에 맞게 연산자 순서를 지정
# 계산식을 eval함수를 활용해 출력한다.

op = [' ', '+', '-']

def dfs(num, cal):
    if num == N+1:
        if eval(cal.replace(' ','')) == 0:
            print(cal)
        return
    for i in op:
        dfs(num+1, cal+i+str(num))


T = int(input())

for tc in range(T):
    N = int(input())
    dfs(2, '1')
    print()