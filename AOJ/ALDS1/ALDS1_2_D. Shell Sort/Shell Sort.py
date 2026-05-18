import sys
input = sys.stdin.readline

cnt = 0
def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

def shellSort(A, n):
    global cnt 
    cnt = 0
    G = []
    h = 1
    while h <= n:
        G.append(h)
        h = 3 * h + 1
    G.reverse()
    m = len(G)
    for i in range(m):
        insertionSort(A, n, G[i])
    print(m)
    print(*G)
    print(cnt)
    for i in range(n):
        print(A[i])

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

shellSort(A, n)
        



