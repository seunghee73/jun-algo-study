N= int(input())
dice = list(map(int,input().split()))
if N==1:
    print(sum(dice)-max(dice))
    exit()

num = [min(dice[0],dice[5]),min(dice[1],dice[4]), min(dice[2],dice[3])]
num.sort()
#3면
A = sum(num)
#2면
B = sum(num[0:2])
#1면
C = min(dice)

result=0
#맨위층 꼭짓점
result += 4 * A
#모서리
result += ((N-1)*4 + (N-2)*4)*B
#옆면의 면
result += ((N-2)*(N-1))*4*C
#윗면의 면
result += ((N-2)**2)*C

print(result)
