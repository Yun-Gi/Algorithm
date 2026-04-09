A1 = int(input())
A2 = int(input())
A3 = int(input())
#각 3개 입력받기

if A1+A2+A3 != 180:
    print("Error")

else:
    if A1 == 60 and A2 == 60:
        print("Equilateral")
    elif A1 == A2 or A1 == A3 or A2 == A3:
        print("Isosceles")
    else:
        print("Scalene")