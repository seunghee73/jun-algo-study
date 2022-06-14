## 갓승희님꺼 보고 배웠읍니다..
## dp[i] 는 i번쨰 글자부터 마지막 글자까지의 단어목록의 단어를 만들수있는지를 나타냅니당
word = input()
n = int(input())
lst = []
dp = [0] * len(word) + [1]
for _ in range(n):
    lst.append(input())
for i in range(len(word)-1,-1,-1):
    for j in lst:
        if word[i:i+len(j)] == j and dp[i+len(j)] == 1:
            dp[i] = 1
print(dp[0])