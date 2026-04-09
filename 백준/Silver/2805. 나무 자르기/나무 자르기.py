import sys
input = sys.stdin.readline

def binary_search(arr, target):
    arr.sort()
    start = 0
    end = arr[-1]
    
    while start <= end:
        mid = (start + end) // 2
        s = 0
        for i in arr:
            if i > mid:
                s += i - mid
        if s >= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

N, M = map(int,input().split())

lst = list(map(int, input().split()))

print(binary_search(lst, M))