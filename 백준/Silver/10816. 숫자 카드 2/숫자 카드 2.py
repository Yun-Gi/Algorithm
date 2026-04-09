N = int(input())

C = list(map(int,input().split()))

CC = {}
for i in C:
    if i in CC:
        CC[i] += 1
    else:
        CC[i] = 1

M = int(input())
Q = list(map(int,input().split()))

for i in Q:
    if i in CC:
        print(CC[i],end=" ")
    else:
        print(0, end=" ")