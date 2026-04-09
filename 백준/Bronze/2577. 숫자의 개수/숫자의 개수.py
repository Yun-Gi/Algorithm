a = int(input())
b = int(input())
c = int(input())

d = a*b*c

n = [0] * 10

d = str(d)
lst = list(d)

for i in lst:
    if i == "0":
        n[0] += 1
    elif i == "1":
        n[1] += 1
    elif i == "2":
        n[2] += 1
    elif i == "3":
        n[3] += 1
    elif i == "4":
        n[4] += 1
    elif i == "5":
        n[5] += 1
    elif i == "6":
        n[6] += 1
    elif i == "7":
        n[7] += 1
    elif i == "8":
        n[8] += 1
    elif i == "9":
        n[9] += 1

for i in range(10):
    print(n[i])