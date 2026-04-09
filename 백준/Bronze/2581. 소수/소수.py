M = int(input())
N = int(input())

sum = 0
min = 10001

for i in range(M,N+1):
    T = 0
    for j in range(1,i):
        if i % j == 0:
            T += 1
    if T == 1:
        sum += i
        if i <= min:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)