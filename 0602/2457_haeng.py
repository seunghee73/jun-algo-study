N=int(input())

flower =[]
for _ in range(N):
    a,b,c,d = input().split()
    if len(b) == 1:
        b = '0' + b
    if len(d) == 1:
        d = '0' + d
    if a+b == c+d:
        continue
    flower.append((int(a+b),int(c+d)))
flower.sort()

start=0
end=0
for i in flower:        #3월1일부터 or 11월30일 이후로 지는 꽃이 없으면 0출력
    if i[0] <= 301:
        start += 1
    if i[1] > 1130:
        end += 1
if end == 0 or start==0:
    print(0)
    exit()

select=(301,301)
for i in range(len(flower)):        #가장 처음 필 꽃 찾기
    if flower[i][0] <= 301 and flower[i][1] > select[1]:
        select = flower[i]
    elif flower[i][0] > 301:
        break

result = 1
last = select[1]
while last < 1201:  #마지막 핀 꽃이 12월1일이 넘어갈떄까지 다음꽃 찾기
    save = select
    for i in range(len(flower)):
        if flower[i][0] <= last and flower[i][1] > select[1]:       #앞선 꽃을 이어갈 꽃 찾기
            select=flower[i]
        elif flower[i][0] > last:      #더 이어나갈수 없을경우
            if save == select:
                print(0)
                exit()
            break
    last = select[1]        # 찾은 꽃 지는날 저장, 꽃 개수 카운트
    result += 1
print(result)