X = int(input())

Num = 1
BNum = 0
jump = 1

for i in range(1,10000000):
    if X <= Num:
        X -= BNum
        if i % 2 == 0:
            print(f"{X}/{i+1-X}")
        else:
            print(f"{i+1-X}/{X}")
        break
    jump += 1
    BNum = Num
    Num += jump