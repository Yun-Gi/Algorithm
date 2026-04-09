N, B = input().split()
B = int(B)
sum = 0

for i in range(len(N)-1,-1,-1):
    if N[i].isalpha():
        sum += (ord(N[i]) - ord('A') + 10) * B **(len(N)-(i+1))
    else:
        sum += int(N[i]) * B**(len(N)-(i+1))
print(sum)
