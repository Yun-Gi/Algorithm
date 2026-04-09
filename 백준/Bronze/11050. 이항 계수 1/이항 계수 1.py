N, K = map(int, input().split())
u = 1 
d = 1

for i in range(N,N-K,-1):
    u *= i 

for j in range(1,K+1):
    d *= j 

print(u//d) 