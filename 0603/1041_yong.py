# 각 면에 따라 정해진 규칙이 존재
# 마주보는 면의 최소값을 기반으로 풀 수 있었던 문제
# -------------------------------------
# N이 1인경우를 고려안해수 수정

N = int(input())
ans = 0
lst = list(map(int, input().split()))
if N == 1:
    lst.sort()
    ans = sum(lst[:5])
else:
    v = []
    v.append(min(lst[0], lst[5]))
    v.append(min(lst[1], lst[4]))
    v.append(min(lst[2], lst[3]))
    v.sort()
    ans = sum(v) * 4
    ans += ((N-1)*(N-2) * 4 + (N-2) ** 2) * v[0]
    ans += sum(v[:2]) * (4 * (N-1) + 4 * (N-2)) 
print(ans)