N = int(input())

lst = set()
rlst = [[] for _ in range(51)]

for i in range(N):
    lst.add(input())


for i in range(51):
    for j in lst:
        if len(j) == i:
            rlst[i].append(j)
    rlst[i].sort()

for i in rlst:
    for j in i:
        print(j)