# 01, 10 순서로 replace를 활용하여 입력값을 변형
# 규칙에 따라 B(10으로 시작)인 경우 판단과 A(01)을 판단하여 기록
# 만약 체크안된 부분이 있다면 노이즈인 것

def B_check(idx):
    check[idx] = 1
    idx += 1
    # while val[idx] == '0':
    while idx < len(val):
        if val[idx] == '0':
            check[idx] = 1
            idx += 1
        else:
            break

    if idx < len(val) and val[idx] == 'A':
        check[idx] = 1
        idx += 1
        # while val[idx] == '1':
        while idx < len(val):
            if val[idx] == '1':
                check[idx] = 1
                idx += 1
            else:
                break
        return True
    else:
        return False


val = input()
val = val.replace('01', 'A')
val = val.replace('10', 'B')
check = [0] * len(val)
if val[0] == 'B' or val[0] == 'A':
    for i in range(len(val)):
        if val[i] == 'B':
            if not B_check(i):
                print('NOISE')
                exit()
        elif not check[i] and val[i] == 'A':
            check[i] = 1
    for i in check:
        if i == 0:
            print('NOISE')
            exit()
    print('SUBMARINE')
else:
    print('NOISE')