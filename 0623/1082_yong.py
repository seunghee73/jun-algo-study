# 그리디로 푼 문제
# 같은 값은 높은 숫자만 필요하기 때문에 딕셔너리로 저장 후 가격순으로 정렬
# 답을 문자형태로 저장 후 출력하기 때문에 000같은 케이스를 방지
N = int(input())
P = list(map(int, input().split()))
M = int(input())

P_dict = dict()
m = 0
num = ''
for i in range(len(P)):
    P_dict[P[i]] = i
P_lst = sorted(P_dict.items())

ans = []
money = []
if len(P_lst) > 1 and P_lst[0][1] == 0:
    if M >= P_lst[1][0]:
        ans.append(P_lst[1][1])
        money.append(P_lst[1][0])
cnt = (M-sum(money)) // P_lst[0][0]

for i in range(cnt):
    ans.append(P_lst[0][1])
    money.append(P_lst[0][0])

rem = M - sum(money)
for i in range(len(money)):
    for j in range(len(P)-1, -1, -1):
        if i == 0:
            if j == ans[i]:
                break
            if P[j] - money[i] <= rem:
                rem -= P[j] - money[i]
                money[i] = P[j]
                ans[i] = j
                break
        else:
            if P[j] == ans[i]:
                for i in range(len(ans)):
                    num += str(ans[i])
                print(int(num))
                exit()
            if P[j] - money[i] <= rem:
                rem -= P[j] - money[i]
                money[i] = P[j]
                ans[i] = j
                break

for i in range(len(ans)):
    num += str(ans[i])
print(int(num))
