N = int(input())
a = [6]
a = list(map(int,input().split()))
T, P = map(int,input().split())

tb = 0
pb, pe = 0, 0

for i in range(6):
    if a[i] % T != 0:
        tb += (a[i] // T) + 1
    else:
        tb += (a[i] // T)
print(tb)
print(N//P, N%P)