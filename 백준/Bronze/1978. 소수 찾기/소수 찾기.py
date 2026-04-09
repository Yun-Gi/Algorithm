N = int(input())
X = 0

list = []
list.extend(map(int,input().split()))

for i in list:
    M = 0
    if i != 1:
        for j in range(1,i):
            if i % j == 0:
                M += 1
    if M == 1:
        X += 1

print(X)
