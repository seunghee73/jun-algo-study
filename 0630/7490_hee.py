from collections import deque
T = int(input())

def cal(txt):
    ST_num = deque([])
    ST_exq = deque([])
    temp = ''
    for i in txt:
        if i.isdigit():
            temp += i
        else:
            if i == ' ':
                pass
            else:
                ST_exq.append(i)
                ST_num.append(int(temp))
                temp = ''
    ST_num.append(int(temp))

    while ST_exq:
        a = ST_num.popleft()
        b = ST_num.popleft()
        c = ST_exq.popleft()
        if c == '+':
            ST_num.appendleft(a + b)
        elif c == '-':
            ST_num.appendleft(a - b)

    return ST_num[0]

def func(idx, txt):
    if idx == N+1:
        if cal(txt) == 0:
            ans.append(txt)
        return

    func(idx+1, txt + '+' + str(idx))
    func(idx+1, txt + '-' + str(idx))
    func(idx+1, txt + ' ' + str(idx))

for t in range(T):
    N = int(input())
    ans = []
    func(2, '1')
    ans.sort()
    for i in ans:
        print(i)
    print()