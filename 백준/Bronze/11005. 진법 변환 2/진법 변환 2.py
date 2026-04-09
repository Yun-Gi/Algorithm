N, B = input().split()
N = int(N)
B = int(B)
sum = ""

while(N>0):
    i = N % B
    if(i>=10):
        i=chr(i+ord('A') - 10)
    else:
        i = str(i)
    sum = i + sum

    N = N//B

print(sum)