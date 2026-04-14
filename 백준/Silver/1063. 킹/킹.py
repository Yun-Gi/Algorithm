import sys
input = sys.stdin.readline

king, stone, N = input().split()

N = int(N)
KingC, KingR = king.strip()
StoneC, StoneR = stone.strip()
KingL = [0, 0]
StoneL = [0, 0]
KingL[0] = ord(KingC) - ord('A') + 1
StoneL[0] = ord(StoneC) - ord('A') + 1 
KingL[1] = int(KingR)
StoneL[1] = int(StoneR)


#아스키코드 변환은 ord, 다시 문자는 chr
def move(uInput):
    if uInput == 'R':
        if KingL[0]+1 == StoneL[0] and KingL[1] == StoneL[1]:
            if StoneL[0] < 8:
                KingL[0] += 1
                StoneL[0] += 1
        elif KingL[0] < 8:
            KingL[0] += 1
    if uInput == 'L':
        if KingL[0]-1 == StoneL[0] and KingL[1] == StoneL[1]:
            if StoneL[0] > 1:
                KingL[0] -= 1
                StoneL[0] -= 1
        elif KingL[0] > 1:
            KingL[0] -= 1
    if uInput == 'B':
        if KingL[0] == StoneL[0] and KingL[1]-1 == StoneL[1]:
            if StoneL[1] > 1:
                KingL[1] -= 1
                StoneL[1] -= 1
        elif KingL[1] > 1:
            KingL[1] -= 1             
    if uInput == 'T':
        if KingL[0] == StoneL[0] and KingL[1]+1 == StoneL[1]:
            if StoneL[1] < 8:
                KingL[1] += 1
                StoneL[1] += 1
        elif KingL[1] < 8:
            KingL[1] += 1
    if uInput == 'RT':
        if KingL[0]+1 == StoneL[0] and KingL[1]+1 == StoneL[1]:
            if StoneL[0] < 8 and StoneL[1] < 8:
                KingL[0] += 1
                KingL[1] += 1
                StoneL[0] += 1
                StoneL[1] += 1
        elif KingL[0] < 8 and KingL[1] < 8:
            KingL[0] += 1
            KingL[1] += 1
    if uInput == 'LT':
        if KingL[0]-1 == StoneL[0] and KingL[1]+1 == StoneL[1]:
            if StoneL[0] > 1 and StoneL[1] < 8:
                KingL[0] -= 1
                KingL[1] += 1
                StoneL[0] -= 1
                StoneL[1] += 1
        elif KingL[0] > 1 and KingL[1] < 8:
            KingL[0] -= 1
            KingL[1] += 1
    if uInput == 'RB':
        if KingL[0]+1 == StoneL[0] and KingL[1]-1 == StoneL[1]:
            if StoneL[0] < 8 and StoneL[1] > 1:
                KingL[0] += 1
                KingL[1] -= 1
                StoneL[0] += 1
                StoneL[1] -= 1
        elif KingL[0] < 8 and KingL[1] > 1:
            KingL[0] += 1
            KingL[1] -= 1
    if uInput == 'LB':
        if KingL[0]-1 == StoneL[0] and KingL[1]-1 == StoneL[1]:
            if StoneL[0] > 1 and StoneL[1] > 1:
                KingL[0] -= 1
                KingL[1] -= 1
                StoneL[0] -= 1
                StoneL[1] -= 1
        elif KingL[0] > 1 and KingL[1] > 1:
            KingL[0] -= 1
            KingL[1] -= 1

for _ in range(N):
    move(input().strip())

KingL[0] = chr(KingL[0]+64)
StoneL[0] = chr(StoneL[0]+64)

print("".join(map(str, KingL)))
print("".join(map(str, StoneL)))