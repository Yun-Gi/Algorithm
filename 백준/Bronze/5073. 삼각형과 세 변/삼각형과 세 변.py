A1,A2,A3 = map(int,input().split())

while not(A1==A2==A3==0):
    if (A1+A2+A3)-max(A1,A2,A3) <= max(A1,A2,A3): 
        print("Invalid")

    else:
        if A1==A2==A3:
            print("Equilateral")
        elif A1 == A2 or A1 == A3 or A2 == A3:
            print("Isosceles")
        else:
            print("Scalene")
    
    A1,A2,A3 = map(int,input().split())