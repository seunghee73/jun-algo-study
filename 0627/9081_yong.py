# 규칙을 찾아 구현하는 문제
# 문자열끼리는 비교 가능(대, 소문자 구분)
# 사전순 정렬 규칙에 맞게 구현

T = int(input())
for tc in range(T):
    flag = False
    word = list(input())
    for i in range(len(word)-1, 0, -1):
        if word[i] > word[i-1]:
            for j in range(len(word)-1, i-1, -1):
                if word[i-1] < word[j]:
                    word[i-1], word[j] = word[j], word[i-1]
                    temp = sorted(word[i:])
                    word = word[:i] + temp
                    flag = True
                    break
        if flag:
            break

    print("".join(word))