#220627 9081 단어 맞추기
# 주어진 단어의 알파벳으로 만들수있는 단어들을 사전순 정렬할때
# 주어진 단어의 다음에 나오는 단어를 출력하라
# string < 100
# 주어진게 마지막 순서라면 그냥 그놈 출력
# 백트래킹으로 원래 단어나오면 그다음 단어 출력?..
# 100^100아닌가 그럼?
# 마지막 글씨부터 해당것보다 큰거 찾기
# 찾으면 그 앞에 껴주고 뒤에있는 애들 sorted
# 없으면 마지막 글씨 앞으로 넘어가기
import sys
input = sys.stdin.readline

tc_num = int(input())
for tc in range(tc_num):
    getString = list(input().rstrip())
    # print(list(map(ord,getString)), list(map(ord,sorted(getString))))
    answer = []
    check = True

    for idx in range(len(getString)-1,0,-1):
        if getString[idx-1] < getString[idx]:
            getIdx = idx
            check = False
            break
    if check:
        print("".join(getString))
    else:
        minStr = max(getString)
        minIdx = -1
        check = False
        for idx in range(getIdx-1,len(getString)):
            if getString[idx] > getString[getIdx-1]:
                minStr = getString[idx]
                minIdx = idx
                check = True
        getString[getIdx-1], getString[minIdx] = getString[minIdx], getString[getIdx-1]
        answer = getString[:getIdx]
        answer.extend(sorted(getString[getIdx:]))
        print("".join(answer))