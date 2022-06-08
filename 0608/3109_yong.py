# 상단부터 갈 수 있는 경로를 찾아 기록하는 방식
# 재귀를 사용하지 않을 시 경로를 찾는데 문제가 발생해 재귀를 이용한 방식으로 수정

d = [-1, 0, 1]

def root(y, x):
    if x == C-1:
        return True
    for dy in d:
        if 0 <= y + dy < R and arr[y+dy][x+1] == '.' and not check[y+dy][x+1]:
            check[y+dy][x+1] = 1
            if root(y+dy, x+1):
                return True
    return False

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
check = [[0] * C for _ in range(R)]
ans = 0
for i in range(R):
    if arr[i][0] == '.':
        if root(i, 0):
            ans += 1

print(ans)