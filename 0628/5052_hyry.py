import sys
input = sys.stdin.readline


class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.no_integrity = False

    def insert(self, word):
        cur = self.root
        length = len(word)

        for idx in range(length):
            if cur.end_of_word:
                self.no_integrity = True
                break

            if word[idx] not in cur.children:
                cur.children[word[idx]] = Node()

            cur = cur.children[word[idx]]

        if cur.children: self.no_integrity = True
        cur.end_of_word = True


t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    trie = Trie()
    ans = 'YES'
    for _ in range(n):
        phone = input().rstrip()
        trie.insert(phone)
        if trie.no_integrity:
            ans = 'NO'
    print(ans)
    #         print('NO')
    #         break      오류 발생 -> 테케는 break한다고 안 들어오는 게 아니니까
    # else: print('YES')
