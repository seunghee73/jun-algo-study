# 각 면에 따라 정해진 규칙이 존재
# 마주보는 면의 최소값을 기반으로 풀 수 있었던 문제

N = int(input())
cnt = N * N * 5 - 12 - (N-1)*(N-2) * 4 - (N-2) ** 2
ans = 0
lst = list(map(int, input().split()))
v = []
v.append(min(lst[0], lst[5]))
v.append(min(lst[1], lst[4]))
v.append(min(lst[2], lst[3]))
v.sort()
ans = sum(v) * 4
ans += ((N-1)*(N-2) * 4 * min(lst) + (N-2) ** 2 * min(lst))
ans += (sum(v[:2]) * cnt//2)
print(ans)