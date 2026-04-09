a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())

result = 1

for n in range(n0,101): 
    if a1*n+a0 > c*n:
        result = 0
        break

print(result)