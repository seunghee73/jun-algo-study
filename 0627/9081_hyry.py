
T = int(input())
for _ in range(T):

    words = input()
    newWords = [words[-1]]

    ans = words
    for i in range(len(words) - 2, -1, -1):
        newWords.append(words[i])
        if words[i] < words[i + 1]:
            minW = 'Z' * 101
            tail = ''
            for w in newWords:
                if w > words[i] and minW > w:
                    minW = w
                tail += w
            ans = words[:i] + minW + ''.join(sorted(tail)).replace(minW, '', 1)
            break
    print(ans)

'''
AZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZA
'''