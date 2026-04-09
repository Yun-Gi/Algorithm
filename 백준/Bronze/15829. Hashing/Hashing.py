L = int(input())
hash = input()
sum = 0

for i in range(L):
    sum += (ord(hash[i]) - 96) * 31 ** i

sum %= 1234567891
print(sum)