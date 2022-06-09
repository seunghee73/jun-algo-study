#220607 2671 잠수함식별
# 주어진 패턴인지 아닌지 확인하라 -> 문제이해하는데 23분걸렸네
# (100~1~|01)~ == 100~1~ 과 01을 임의로 섞어서 만들 수 있는 str 집합

getStr = input()

idx = 0
end = len(getStr)
check = True
exStr = -1 # 이전 str이 100~1~ 이면 1/ 01이면 2/ 그외는 -1

while idx < end:
    # print(idx, exStr)
    if getStr[idx] == "1":
        if getStr[idx:idx+3] == "100":
            for nxtIdx in range(idx+2,end):
                if getStr[nxtIdx] == "1":
                    idx = nxtIdx + 1
                    exStr = 1
                    check = False
                    break
            else:
                print("NOISE")
                exit()
        elif exStr == 1:
            idx += 1
        else:
            print("NOISE")
            exit()
    elif getStr[idx] == "0":
        if getStr[idx:idx+2] == "01":
            idx = idx + 2
            exStr = 2
        # elif exStr == 1:
        #     idx += 1
        else:
            print("NOISE")
            exit()
    else:
        if exStr == 1:
            idx += 1
        else:
            print("NOISE")
            exit()
print("SUBMARINE")



