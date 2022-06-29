def check(lst):
    st = [lst[1]]
    visit = {lst[1]}

    while st:
        curV = st.pop()
        tmpR, tmpC = curV // 5, curV % 5

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = tmpR + dr, tmpC + dc
            newV = newR * 5 + newC
            if 0 <= newR < 5 and 0 <= newC < 5 and newV not in visit and newV in lst:
                st.append(newV)
                visit.add(newV)

    if len(visit) == 7: return True
    return False


def comb(depth, min_idx, y_cnt):
    global cnt

    if y_cnt > 3:
        return

    if depth == 7:
        if check(pos):
            cnt += 1
        return

    for num in range(min_idx, 25):
        if not visit[num]:
            visit[num] = True
            pos[depth] = num
            if MAP[num // 5][num % 5] == 'Y':
                comb(depth + 1, num + 1, y_cnt + 1)
            else:
                comb(depth + 1, num + 1, y_cnt)
            visit[num] = False


MAP = [list(input()) for _ in range(5)]
pos = [-1] * 7
visit = [False] * 25
cnt = 0
comb(0, 0, 0)
print(cnt)
