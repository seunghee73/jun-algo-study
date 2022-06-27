T = int(input())

for _ in range(T):
    A = list(input())

    val1, val2 = 0, 1
    for i in range(len(A)-1, 0, -1):
        if A[i-1] < A[i]:
            val1 = i-1
            break
    else:
        print(''.join(A))
        continue

    for i in range(len(A)-1, 0, -1):
        if A[val1] < A[i]:
            val2 = i
            break

    A[val1], A[val2] = A[val2], A[val1]
    temp = reversed(list(A[val1+1:]))
    A[val1+1:] = temp
    print(''.join(A))
