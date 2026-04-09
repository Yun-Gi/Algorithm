N = int(input())

xy = [list(map(int,input().split())) for _ in range(N)]
lst = [1] * N
num = 0

for i in xy:
    for j in xy:
        if i[0]<j[0] and i[1]<j[1]:
            lst[num] += 1
    num += 1

print(*(lst[i] for i in range(N)), end=" ")