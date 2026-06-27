import sys
input = sys.stdin.readline

def select(i, m, n, A):
    if m == 0:
        return True
    if i >= n:
        return False
    return select(i + 1, m, n, A) or select(i + 1, m - A[i], n, A)
    

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

for mi in m:
    if select(0, mi, n, A):
        print('yes')
    else:
        print('no')

