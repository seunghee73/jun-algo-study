S = list(input())
N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))

D = [0] * len(S) + [1]
for i in range(len(S)-1, -1, -1):
    for a in A:
        if (S[i:i+len(a)] == a) and D[i+len(a)] == 1:
            D[i] = 1
print(D[0])