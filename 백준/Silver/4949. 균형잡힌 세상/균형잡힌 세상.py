lst = input()

while len(lst) != 1 and lst[0] != ".":
    sublst = []
    b = 0
    for i in lst:
        if i == "(" or i == "[":
            sublst.append(i)
        elif i == ")" :
            if len(sublst) != 0 and sublst[-1] == "(":
                sublst.pop()
            else:
                b += 1
                
        elif i == "]":
            if len(sublst) != 0 and sublst[-1] == "[":
                sublst.pop()
            else:
                b += 1

    if len(sublst) == 0 and b == 0:
        print("yes")
    else:
        print("no")

    lst = input()         