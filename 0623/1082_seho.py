#220623 1082 방번호
# 주어진 예산 m으로 큰 정수 값을 갖는 비밀번호 만들기
# m+1 길이의 lst 0부터 최적 값 찾기.
# 알고리즘 유형은 예상이 가는데 구상이 안되네..
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
answers = [[] for _ in range(m+1)]
answers[0] = ""

for cost in range(1,m+1):
    for idx in range(n):
        exIdx = cost-lst[idx]
        if exIdx >= 0:
            if answers[exIdx] or answers[exIdx] == "":
                answers[cost].append(str(idx)+answers[exIdx])
                answers[cost].append(answers[exIdx] + str(idx))
    if answers[cost]:
        # print(answers[cost])
        answers[cost] = str(max(list(map(int,answers[cost]))))
result = 0
# print(answers)
for ans in answers:
    if ans:
        result =max(int(ans),result)
print(result)
