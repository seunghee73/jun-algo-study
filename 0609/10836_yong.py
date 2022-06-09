# 그리디 문제
# 활용할 장소와 필요없는 장소가 있기 때문에 모든 배열을 만들지 않았음
# [1, 1]부터 [M-1, M-1]은 패턴이 같기 때문에 배열에 저장해서 사용했지만 시간차이가 많이남

import sys
input = sys.stdin.readline

M, N = map(int ,input().split())
arr = [1] * (2*M-1)

for _ in range(N):
    day = list(map(int, input().split()))
    grow = [0] * day[0] + [1] * day[1] + [2] * day[2]

    for val in range(M):
        arr[val] += grow[val]

    for val in range(M-1):
        arr[M+val] += grow[M+val]


ans = arr[M:]
for i in range(M-1, -1, -1):
    print(arr[i], end=' ')
    print(*ans)