import re

A = input()
P = re.compile('(100+1+|01)+')
ans = P.fullmatch(A)
if ans:
    print('SUBMARINE')
else:
    print('NOISE')

# match()는 문자열의 처음부터 시작해서 작성한 패턴이 일치하는지 확인
# search()는 match()와 유사하지만 패턴이 문자열의 처음부터 일치하지 않아도 괜찮
# findall()은 문자열 안에 패턴에 맞는 케이스를 전부 찾아서 리스트로 반환
# fullmatch()는 문자열 전체가 해당 패턴일 때 반환
# 패턴과 일치하는 접두사가 있는지를 판단하려면 match 문자열 전체가 패턴과 일치하느냐를 검사하려면 fullmatch