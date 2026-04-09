T = int(input())

for _ in range(T):
    PS = input()
    lst = []
    B = True
    for i in PS:
        if i == "(":
            lst.append(i)
        elif i == ")" and len(lst) != 0:
            lst.pop()
        else:
            B = False
            break
    if len(lst) == 0 and B == True:
        print("YES")
    else:
        print("NO")