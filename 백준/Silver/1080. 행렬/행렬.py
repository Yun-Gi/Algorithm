import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [list(map(int, list(input().strip()))) for _ in range(N)]
B = [list(map(int, list(input().strip()))) for _ in range(N)]

def flip(lst ,x, y):
    for i in range(3):
        for j in range(3):
            lst[x+i][y+j] = 1 - lst[x+i][y+j]

count = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(A, i, j)
            count += 1

if A == B:
    print(count)
else:
    print(-1)