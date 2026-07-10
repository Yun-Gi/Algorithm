import sys
input = sys.stdin.readline

def mergeSort(A, left, right):
    if left+1 >= right:
        return 0
    
    mid = (left + right)//2
    count = 0

    count += mergeSort(A, left, mid)
    count += mergeSort(A, mid, right)

    count += merge(A, left, mid, right)

    return count

def merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]

    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    count = 0

    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            count += (len(L) - 1 - i)
    return count

n = int(input())
A = list(map(int, input().split()))
print(mergeSort(A,0,n))

