n = int(input())
arr = []
for _ in range(n):
    lst = list(map(int, input().split()))
    arr.append([lst[0]*100 + lst[1], lst[2]*100+lst[3]])

arr.sort(key=lambda x:x[1])
arr.sort()


cnt = 0
end = 0
stand = 301

while arr:
    if stand >=1201 or stand < arr[0][0]:
        break
    for _ in range(len(arr)):
        if stand >= arr[0][0]:
            if end <= arr[0][1]:
                end = arr[0][1]
            arr.remove(arr[0])
        else:
            break

    stand = end
    cnt += 1
if stand >= 1201:
    print(cnt)
else:
    print(0)
