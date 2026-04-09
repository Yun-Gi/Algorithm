A,B = map(int,input().split())
C, D = 1, 0

for i in range(2,10000):
    if A%i==0 and B%i==0:
        C = i

D = (A*B) // C

print(C)
print(D)