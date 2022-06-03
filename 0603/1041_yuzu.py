corner = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]
side = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

n = int(input())
dice = list(map(int, input().split()))
one = min(dice)
two = 100
for s in side:
    if two > dice[s[0]]+dice[s[1]]:
        two = dice[s[0]]+dice[s[1]]
three = 150
for c in corner:
    if three > dice[c[0]]+dice[c[1]]+dice[c[2]]:
        three = dice[c[0]]+dice[c[1]]+dice[c[2]]

ans = 0
if n == 1:
    ans = sum(dice)-max(dice)
else:
    ans += three*4
    ans += two*(8*n-12)
    if n >= 3:
        ans += one*(5*(n**2)-(16*n)+12)
print(ans)