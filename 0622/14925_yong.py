# DP문제
# 정사각형을 판단하기 위에 좌측, 위쪽, 대각선 방향의 값중 최소값의 +1값을 DP에 저장한다

M, N = map(int ,input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
DP = [[0] * (N+1) for _ in range(M+1)]
ans = 0
for i in range(1, M+1):
    for j in range(1, N+1):
        if not arr[i-1][j-1]:
            DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])+1
            ans = max(DP[i][j], ans)
print(ans)