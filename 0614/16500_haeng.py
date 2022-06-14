S = input()
N = int(input())
word = []
for _ in range(N):
    word.append(input())

dp = [[] for _ in range(100)]

for j in word:
    if j in S:
        dp[0].append(j)
s=0
for i in range(1,101):  # 만약 word가 한글자이고 S가 100글자일경우 100번해야함
    if S in dp[i-1]:
        s=1
        break

    for j in word:
        if j in S:                  #해당 단어가 S에 들어있을경우에만
            for k in dp[i-1]:       #이전에 작업한거에 더해보기
                A = k +j
                if len(A) <= 100 and A in S and A not in dp[i]:  #더한값이 S로 만들어질수 있을경우에만 dp에 저장, 100자넘으면 안됨
                    dp[i].append(A)
if s:
    print(1)
else:
    print(0)