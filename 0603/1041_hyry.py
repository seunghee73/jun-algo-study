
def cube():
    if N == 1:
        return sum(dice) - max(dice)

    three = [
        (0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4),
        (1, 3, 5), (1, 2, 5), (3, 4, 5), (2, 4, 5)
    ]

    two = [
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 3), (1, 5),
        (2, 4), (2, 5),
        (3, 4), (3, 5),
        (4, 5),
    ]

    one = min(dice)
    ans1 = one * ((N - 2) * (N - 1) * 4 + (N - 2) * (N - 2))

    ans2 = 1e10
    for a, b in two:
        if ans2 > dice[a] + dice[b]:
            ans2 = dice[a] + dice[b]

    ans2 = ans2 * ((N - 2) * 8 + 4)

    ans3 = 1e10
    for x, y, z in three:
        if ans3 > dice[x] + dice[y] + dice[z]:
            ans3 = dice[x] + dice[y] + dice[z]

    ans3 = ans3 * 4

    if N == 2:
        return ans2 + ans3

    return ans1 + ans2 + ans3


N = int(input())
dice = list(map(int, input().split()))

print(cube())