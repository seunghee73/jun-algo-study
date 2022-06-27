# 220628 5052 전화번호 목록
# 오잉 옛날 프로그래머스에서 보았던?.. 파싱어쩌고?..
# n <= 10,000, 전화번호는 10자리
import sys

input = sys.stdin.readline

tc_num = int(input())

for tc in range(tc_num):
    n = int(input())
    lst = [input().rstrip() for _ in range(n)]
    lst.sort()
    # print(lst)

    answer = "YES"

    for idx in range(len(lst)-1):
        if lst[idx] == lst[idx+1][:len(lst[idx])]:
            answer = "NO"
            break
    print(answer)
