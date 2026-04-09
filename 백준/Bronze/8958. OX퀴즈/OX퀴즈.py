a = int(input())

for i in range(a):
    b = input()
    c = list(b)
    point = 0
    sum = 0
    for j in range(len(c)):
        if c[j] == "X":
            point = 0
            sum += point
        if c[j] == "O":
            point += 1
            sum += point
    print(sum)