# 문자열을 비교하여 겹치는 부분이 있나 판단하는 문제
# 문자형 데이터의 정렬을 활용하여 앞뒤만 비교해 풀 수 있는문제

import sys
input = sys.stdin.readline

def check():
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            return True
    return False


t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip('\n'))
    arr.sort()
    if check():
        print('NO')
    else:
        print('YES')