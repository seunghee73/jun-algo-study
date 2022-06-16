
import sys
input = sys.stdin.readline

# 사실 하우상좌로 하면 이진법과 같지만
# 이게 더 편해서 선택
notWalls = [
    (-1, -1, -1, -1), (1, 1, 0, 1), (0, 1, 1, 1), (0, 1, 0, 1),
    (1, 1, 1, 0), (1, 1, 0, 0), (0, 1, 1, 0), (0, 1, 0, 0),
    (1, 0, 1, 1), (1, 0, 0, 1), (0, 0, 1, 1), (0, 0, 0, 1),
    (1, 0, 1, 0), (1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 0)
]


def dfs(row, col, roomNum):
    ST = [(row, col)]
    visited[row][col] = roomNum
    size = 0

    while ST:
        curR, curC = ST.pop()
        size += 1

        for idx, (dr, dc) in enumerate(((-1, 0), (1, 0), (0, -1), (0, 1))):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C:
                if notWalls[MAP[curR][curC]][idx] and not visited[newR][newC]:
                    ST.append((newR, newC))
                    visited[newR][newC] = roomNum
                else:  # 벽인데 번호가 다른 경우 인접 room으로 체크
                    if not notWalls[MAP[curR][curC]][idx] and visited[newR][newC] not in (0, roomNum):
                        adj.add((roomNum, visited[newR][newC]))

    return size


C, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)] # visited에 각 room 마다 번호 붙이기
roomNum = oneRoom = twoRoom = 0

roomSizes = dict()  # 방 번호마다 크기 기억용
adj = set()  # 인접한 방 쌍으로 저장
for row in range(R):
    for col in range(C):
        if not visited[row][col]:
            roomNum += 1
            size = dfs(row, col, roomNum)
            roomSizes[roomNum] = size
            if oneRoom < size:
                oneRoom = size

# 인접한 애들끼리 방 크기 더해서 최대값 구하기
for r1, r2 in adj:
    if twoRoom < roomSizes[r1] + roomSizes[r2]:
        twoRoom = roomSizes[r1] + roomSizes[r2]

print(roomNum, oneRoom, twoRoom, sep="\n")