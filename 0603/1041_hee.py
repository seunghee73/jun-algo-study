import sys
INF = sys.maxsize
N = int(input())
A, B, C, D, E, F = list(map(int, input().split()))
dice = [A, B, C, D, E, F]

# 주사위의 서로 인접하고 합이 제일 작은 세 면 찾기
val = min(A, F)
min_sum = INF
for i in [(B, C), (C, E), (E, D), (D, B)]:
    if sum(i) < min_sum:
        temp = i
        min_sum = sum(i)
vals = sorted([val, temp[0], temp[1]])

corner = 4
edge = 4 * (N-1) + 4 * (N-2)
face = (N-1) * (N-2) * 4 + (N-2) * (N-2)

# 꼭짓점의 경우 세 면의 합, 모서리의 경우 두 면의 합, 면의 경우 한 면의 합
ans = 0
ans += (vals[0] + vals[1] + vals[2]) * corner
ans += (vals[0] + vals[1]) * edge
ans += (vals[0]) * face

if N == 1:
    print(sum(dice) - max(dice))
else:
    print(ans)
