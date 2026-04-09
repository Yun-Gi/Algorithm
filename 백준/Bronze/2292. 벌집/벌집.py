N = int(input())

i = 1
j = 6
s = 1
while True:
     if N <= i:
        print(s)
        break
     else:
         s+=1
         i+=j
         j+=6