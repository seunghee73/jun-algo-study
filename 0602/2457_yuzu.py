import sys
input = sys.stdin.readline

n = int(input())
day = []
for _ in range(n):
    sx, sy, ex, ey = map(int, input().split())
    day.append([100*sx+sy, 100*ex+ey])
day.sort()

now = 0
end = 301
ans = 0
while day:
    if end > 1130 or end < day[0][0]:
        break
    for _ in range(len(day)):
        if end >= day[0][0]:
            if now <= day[0][1]:
                now = day[0][1]
            day.pop(0)
        else:
            break
    end = now
    ans += 1

print(0) if end < 1201 else print(ans)