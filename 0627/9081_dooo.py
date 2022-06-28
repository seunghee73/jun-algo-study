import sys

input = sys.stdin.readline


def perm(lst):
    idx = -1
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            idx = i
    if idx == -1:
        return False

    for i in range(len(lst) - 1, -1, -1):
        if lst[idx] < lst[i]:
            c_idx = i
            break

    lst[idx], lst[c_idx] = lst[c_idx], lst[idx]
    sol = lst[:idx+1] + lst[idx+1:][::-1]
    return sol


TC = int(input())
for _ in range(TC):
    s = list(input().strip())
    ans = perm(s)
    if ans:
        print(''.join(ans))
    else:
        print(''.join(s))