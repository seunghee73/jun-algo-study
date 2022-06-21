#2206021 세용액
# n개의 -1억 ~ +1억의 범위를 갖는 수
# n <= 5000
# 3개를 골라 0에 가장 가까운 수?
# start, mid, end 자리의 수를 더하기
# 총합이 양수면 end -= 1/ 음수면 +=1/ 0이면 break
# mid <= end 이면 mid 갱신/ start<mid여도 같이 갱신
# 매번 계산마다 answer 과 절댓값 비교.
# 5
# -10000 -9 10 15 10000
# 8
# -1000 -9 -7 -5 1 7 100 1000
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lst.sort()
# print(lst)
result = float('inf')
answer = []

for s in range(n-2):
    start = lst[s]
    mid = s+1
    end = n-1

    while mid < end:
        output = start + lst[mid] + lst[end]
        if abs(output) < abs(result):
            answer = [start,lst[mid],lst[end]]
            result = output
        if output < 0:
            mid += 1
        elif output > 0:
            end -= 1
        elif output == 0:
            print(*answer)
            exit()
print(*answer)