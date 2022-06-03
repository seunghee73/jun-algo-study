n = int(input())
lst = list(map(int, input().split()))
slst = [min(lst[0], lst[5]), min(lst[1], lst[4]), min(lst[2], lst[3])]
slst.sort()
min_val = slst[0]
min_two = slst[0]+slst[1]
min_three = sum(slst)

if n >=2:
    ans = (4 * min_three) + (4*(2*n-3)) * min_two + (4*(n-1)*(n-2) + (n-2) **2)*min_val

else:
    ans = sum(lst) - max(lst)
print(ans)