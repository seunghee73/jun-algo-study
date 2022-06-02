import sys
input = sys.stdin.readline
day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def trans(m, d): # 월과 일이 몇 번째 날인지 바꿔주는 함수 (ex: 1월 1일 > 1일 , 2월 1일 > 32일)
    val = 0
    for i in range(1, m):
        val += day[i]
    val += d
    return val

N = int(input())
G = []
for _ in range(N): # 월과 일이 주어지면 날로 바꿔서 G에 (피는 날, 지는 날)로 append
    a, b, c, d = map(int, input().split())
    s = trans(a, b)
    e = trans(c, d)
    G.append((s, e))

ps = trans(3, 1) # 시작 날
pe = trans(11, 30) # 마지막 날
G.sort(key=lambda x: (x[0], x[1]))

D = []
for s, e in G:
    if e < ps or pe < s: # 꽃이 지는 날보다 시작 날이 늦거나, 꽃이 피는 날보다 마지막 날이 이른 경우는 넘기기
        continue

    if not D:
        if ps < s: # 시작 날보다 첫 번째 꽃이 피는 날이 늦는 경우는 불가능
            print(0)
            exit(0)
        D.append((s, e))

    elif len(D) == 1: # 시작 날보다 꽃이 피는 날이 이르거나 같으면서 최근 꽃보다 늦게 지면 교체
        if s <= ps and D[-1][1] < e:
            D = [(s, e)]

        elif s <= D[-1][1] < e: # 아니면 추가
            D.append((s, e))
    else: # 2일 전 꽃이 지는 날보다 이르거나 같으면서 최근 꽃보다 늦게 지면 교체
        if s <= D[-2][1] and D[-1][1] < e:
            D[-1] = (s, e)

        elif s <= D[-1][1] < e: # 아니면 추가
            D.append((s, e))

    if pe < D[-1][1]:
        print(len(D))
        break
else:
    print(0)
