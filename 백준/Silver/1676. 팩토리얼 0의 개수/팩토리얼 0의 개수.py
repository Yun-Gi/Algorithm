N = int(input())
pac = 1
num = 0

for i in range(N,1,-1):
    pac *= i

npac = str(pac)



for i in range(len(npac)-1,-1,-1):
    if npac[i] == '0':
        num += 1
    else:
        break

print(num)
        