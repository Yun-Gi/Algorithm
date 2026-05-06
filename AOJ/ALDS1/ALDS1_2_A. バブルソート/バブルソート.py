import sys
input = sys.stdin.readline


def bubbleSort(A, N):
    count = 0
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(N-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                count += 1
                flag = True
        i += 1
        
    return count

N = int(input())
A = list(map(int, input().split()))

count = bubbleSort(A, N)

print(*A)
print(count)