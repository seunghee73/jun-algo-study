N=int(input())
money = list(map(int,input().split()))
M = int(input())

if N==1:
    print(0)
    exit()

max_width = []
c=1
for i in range(1,N):
    if money[i] <= money[c]:
        c = i
max_width.append(c)
M -= money[c]

d=0
for j in range(N):
    if money[j] <= money[d]:
        d = j

while M >= money[d]:
    max_width.append(d)
    M -= money[d]

for k in range(len(max_width)):
    if k == 0:
        for l in reversed(range(N)):
            if money[l] - money[c] <= M:
                max_width[k] = l
                M -= money[l] - money[c]
                break
    else:
        for l in reversed(range(N)):
            if money[l] - money[d] <= M:
                max_width[k] = l
                M -= money[l] - money[d]
                break

result =''
for i in max_width:
    result += str(i)
print(result)


