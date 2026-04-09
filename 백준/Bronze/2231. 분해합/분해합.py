N = int(input())

result = 0

i = 1
while i <= 1000000:
    if (i + i%10 + (i // 10)%10 + 
        (i // 100)%10 + (i // 1000)%10 +
        (i // 10000)%10 + (i // 100000)%10 +
        (i // 1000000)%10) == N :
        result = i
        i = 1000001
    i += 1

print(result)
