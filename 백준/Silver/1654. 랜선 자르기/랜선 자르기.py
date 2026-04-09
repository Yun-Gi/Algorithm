import sys

def binary_search(arr, target):
    start=1 
    end=max(arr)
    
    while start<=end:
        mid=(start+end)//2
        sum=0
        for i in arr:
            sum+=i//mid 
        if sum>=target:
            start=mid+1
        else:
            end=mid-1
    return end

K, N = map(int,sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for _ in range(K)]

print(binary_search(lst,N))