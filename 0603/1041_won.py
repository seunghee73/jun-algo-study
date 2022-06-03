import sys
input = sys.stdin.readline


N = int(input())

arr = list(map(int, input().split()))
dice = []
dice.append(min(arr[0], arr[5]))
dice.append(min(arr[1], arr[4]))
dice.append(min(arr[2], arr[3]))
dice.sort()
arr.sort()

# 위쪽 모서리 4개 + 아래쪽 모서리 4개
res = (dice[0] + dice[1] + dice[2]) * 4 + (dice[0] + dice[1]) * 4

if N == 2:
    print(res)
elif N == 1:
    print(arr[0] + arr[1] + arr[2] + arr[3] + arr[4])
else:
    # 선분 중간부분
    res += (dice[0] + dice[1]) * 8 * (N - 2)
    # 면 중간부분
    res += dice[0] * 5 * (N - 2) ** 2
    # 사이드면 밑부분
    res += dice[0] * 4 * (N - 2)
    print(res)
