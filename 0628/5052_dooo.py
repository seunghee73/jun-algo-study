TC = int(input())
for tc in range(TC):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    lst.sort()
    for i in range(n-1):
        if len(lst[i]) <= len(lst[i+1]):
            if lst[i+1][:len(lst[i])] == lst[i]:
                print('NO')
                break
    else:
        print('YES')
