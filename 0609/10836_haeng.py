M,N = map(int, input().split())
day = []
for _ in range(N):
    day.append(list(map(int,input().split())))

grow = [1]*(2*M-1)

for j in range(N):
    update = [0]*day[j][0] + [1]*day[j][1] + [2]*day[j][2]
    for i in range(2 * M - 1):
        grow[i] += update[i]

#첫칸 뺴고 무조건 위에거와 같다
A = grow[-(M-1):]
grow = grow[:-(M-1)]
for i in range(M):
    print(*([grow.pop()] + A))