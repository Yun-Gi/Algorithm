T = int(input())
C = []
for i in range(T):
    C.append(int(input()))

for i in C:
    print(i // 25,end=" ")
    i = i % 25
    print(i // 10,end=" ")
    i = i % 10
    print(i // 5,end=" ")
    i = i % 5
    print(i // 1)
