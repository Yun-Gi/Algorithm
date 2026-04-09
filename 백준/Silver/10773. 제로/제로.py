K = int(input())
lst = []

for i in range(K):
    N = int(input())
    if N != 0:
        lst.append(N)
    else:
        lst.pop()

print(sum(lst))