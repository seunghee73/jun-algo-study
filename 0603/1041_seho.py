#220603 1041 주사위
# n <= 1,000,000
# 구현
# 완전탐색
# n = 1, 2, 3이상 으로 나누기
n = int(input())
dice = [0]
dice.extend(list(map(int,input().split()))) # A B C D E F
opposites = [0,6,5,4,3,2,1]

if n == 1:
    print(sum(dice)-max(dice))
elif n >= 2:
    sideOne = min(dice[1:])
    sideTwo = float('inf')
    sideTwoIdx =[[1,2],[1,3],[1,4],[1,5],
                 [2,1],[2,3],[2,4],[2,6],
                 [3,1],[3,2],[3,5],[3,6],
                 [4,1],[4,2],[4,5],[4,6],
                 [5,1],[5,3],[5,4],[5,6],
                 [6,2],[6,3],[6,4],[6,5]]
    for idxs in sideTwoIdx:
        sideTwo = min(sideTwo, dice[idxs[0]]+dice[idxs[1]])
    sideThree = float('inf')
    sideThreeIdx = [[1,2,3],[1,2,4],[1,4,5],[1,3,5],
                    [2,3,6],[2,4,6],[3,5,6],[4,5,6]]
    for idxs in sideThreeIdx:
        sideThree = min(sideThree, dice[idxs[0]]+dice[idxs[1]]+dice[idxs[2]])
    result = sideOne*((n-2)**2*5+(n-2)*4)+sideTwo*((n-2)*8+4)+sideThree*4
    print(result)