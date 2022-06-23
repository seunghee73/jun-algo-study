
N = int(input())
arr = list(map(int, input().split()))
M = int(input())


def solution():
    global M

    minNum = minCost = oneMinNum = oneMinCost = 100
    for num, cost in enumerate(arr):
        if minCost >= cost:
            minCost = cost
            minNum = num
        if num > 0 and oneMinCost >= cost:
            oneMinCost = cost
            oneMinNum = num

    bought = []
    if oneMinCost > M:
        bought.append(0)
        return bought
    else:
        bought.append(oneMinNum)
        M -= oneMinCost

    bought += [minNum] * (M // minCost)
    M %= minCost

    if not M: return bought

    for idx, num in enumerate(bought):
        for i in range(N - 1, -1, -1):
            if i > num and M + arr[num] >= arr[i]:
                bought[idx] = i
                M += arr[num]
                M -= arr[i]
                if not M: return bought
                break  # 3%... 

    return bought


ans = ''.join(map(str, solution()))
print(ans)
