from collections import deque

def bfs(words):
    one, two, ans = words
    q = deque([(len(one), len(two), len(ans))])
    visited = [[0] * (len(two)+1) for _ in range(len(one)+1)]
    while q:
        oi, ti, ai = q.popleft()
        if oi == ti == ai == 0:
            return True
        elif ai == 0:
            return False

        if oi > 0 and one[oi-1] == ans[ai-1] and visited[oi-1][ti] == 0:
            visited[oi-1][ti] = 1
            q.append([oi-1, ti, ai-1])
        if ti > 0 and two[ti-1] == ans[ai-1] and visited[oi][ti-1] == 0:
            visited[oi][ti-1] = 1
            q.append([oi, ti-1, ai-1])
    else:
        return False

TC = int(input())
for tc in range(1, TC+1):
    words = list(input().split())
    if bfs(words):
        print("Data set {}: yes".format(tc))
    else:
        print("Data set {}: no".format(tc))