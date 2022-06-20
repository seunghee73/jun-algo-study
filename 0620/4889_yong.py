num = 1
while True:
    # 답 앞에 넘버링용 변수
    string = list(input())
    # 답을 담을 변수
    cnt = 0
    # 종료를 알리는 if문
    if string[0] == '-':
        exit()
    stack = []
    while string:
        val = string.pop(0)
        # 여는 괄호면 그냥 넣기
        if val == '{':
            stack.append(val)
            continue
        # 닫는 괄호일 때
        if val == '}':
            if not stack:
                # 스택이 비어있으면 바꿔서 넣고 cnt +1
                stack.append('{')
                cnt += 1
                continue
            else:
                # 스택이 비어있지않다면 안에 있는거 하나 지우기
                stack.pop()
                continue
    # while을 다 돌고 스택에 남아있는 괄호 // 2개만큼 더하기
    cnt += len(stack) // 2
    print(f'{num}. {cnt}')
    num += 1