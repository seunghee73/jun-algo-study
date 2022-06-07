sound=input()

cnt_1 = 0
while sound:
    if len(sound)>=3 and sound[0] == '1' and sound[1]=='0' and sound[2]=='0':
        if '1' in sound[2:]:
            idx = sound[2:].index('1')
            cnt_1 = 0
            for i in range(2+idx,len(sound)):
                if sound[i] == '1':
                    if i == len(sound)-1:
                        sound=''
                    cnt_1 += 1
                else:
                    sound = sound[i:]
                    break
        else:
            print('NOISE')
            break
    elif sound[0] == '0' and sound[1] =='1':
        sound = sound[2:]

    elif cnt_1 > 1:
        cnt_1 -= 1
        sound = '1' + sound

    else:
        print('NOISE')
        break

if not sound:
    print('SUBMARINE')