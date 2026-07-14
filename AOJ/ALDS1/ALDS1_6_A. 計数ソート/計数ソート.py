import sys
input = sys.stdin.readline

def CountingSort(A, B, k):
    n = len(A)
    C = [0] * (k + 1)
    
    for i in range(n):
        C[A[i]] += 1
        
    for i in range(1, k + 1):
        C[i] = C[i] + C[i-1]
        
    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

n = int(input())
A = list(map(int, input().split()))
B = [0] * (n)

CountingSort(A,B,max(A))

print(*B)
