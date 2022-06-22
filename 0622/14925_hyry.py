import sys
input = sys.stdin.readline

def change(num):
    if num: return 0
    else: return 1


R, C = map(int, input().split())
MAP = [[0] * (C + 1)] +\
      [[0] + list(map(lambda x: change(int(x)), input().split())) for _ in range(R)]

maxArea = 0
for row in range(1, R + 1):
    for col in range(1, C + 1):
        if MAP[row][col]:
            MAP[row][col] = min(
                MAP[row][col - 1],
                MAP[row - 1][col],
                MAP[row - 1][col - 1]
            ) + 1
            if maxArea < MAP[row][col]:
                maxArea = MAP[row][col]

print(maxArea)