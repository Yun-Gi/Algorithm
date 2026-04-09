A1,A2,A3 = map(int,input().split())

if (A1+A2+A3)-max(A1,A2,A3)<=max(A1,A2,A3):
    print(((A1+A2+A3)-max(A1,A2,A3))*2-1)
else:
    print((A1+A2+A3))
