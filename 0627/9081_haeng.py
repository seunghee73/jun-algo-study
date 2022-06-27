T=int(input())
for t in range(T):
    word = list(input())
    result = ''
    for i in reversed(range(1,len(word))):
        if word[i] > word[i-1]:
            save = word[i-1]
            for k in range(i-1):
                result += word.pop(0)
            word.sort()
            for j in range(len(word)):
                if word[j] > save:
                    result += word.pop(j)
                    break
            while word:
                result += word.pop(0)
            break

    if result:
        print(result)
    else:
        for i in word:
            result += i
        print(result)