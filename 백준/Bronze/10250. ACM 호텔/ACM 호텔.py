a = int(input())

for i in range(a):
    q, w, e = map(int,input().split())
    if e % q != 0:
        print((e%q)*100+(1+e//q))
    else:
        print(q*100+e//q)