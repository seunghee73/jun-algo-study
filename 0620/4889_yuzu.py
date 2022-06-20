tc = 1
while True:
    s = list(input())
    ans = 0
    if '-' in s:
        break
    stack = []
    for i in range(len(s)):
        if not stack and s[i] == '}':
            ans += 1
            stack.append('{')
        elif stack and s[i] == '}':
            stack.pop()
        else:
            stack.append(s[i])
    ans += len(stack)//2
    print(f'{tc}. {ans}')
    tc += 1