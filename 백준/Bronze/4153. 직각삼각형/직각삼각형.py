while True:
    a,b,c = map(int,input().split())
    if a == 0 and b==0 and c==0:
        break
    else:
        d = [a,b,c]
        d.sort()
        if (d[2]*d[2]) == (d[0]*d[0]) + (d[1]*d[1]):
            print("right")
        else:
            print("wrong")