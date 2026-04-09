N, M =map(int,input().split())
card=list(map(int,input().split()))
ControlGroup = M
result = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
           if ControlGroup > M - (card[i] + card[j] + card[k]) and M >= (card[i] + card[j] + card[k]):
               ControlGroup = M - (card[i] + card[j] + card[k])
               result = (card[i] + card[j] + card[k])

print(result)   