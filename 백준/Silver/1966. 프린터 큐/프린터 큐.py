def printer(arr:list,N,M):
    counter = 0
    for _ in arr:
        for i in range(N):
            if arr[i] == max(arr) and i == M:
                return counter+1
            elif arr[i] == max(arr):
                arr[i] = 0
                counter += 1
        

C = int(input())

for _ in range(C):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    print(printer(lst,N,M))
