T = int(input())


for _ in range(T):
    re = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
    k = int(input())
    n = int(input())
    for i in range(1,k+1):
        sub = []
        for j in range(0,14):
            if j == 0:
                sub.append(1)
            else:
                sub.append(re[i-1][j]+sub[j-1])
        re.append(sub)
    print(re[k][n-1])