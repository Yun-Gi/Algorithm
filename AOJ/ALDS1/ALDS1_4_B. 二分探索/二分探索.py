import sys
input = sys.stdin.readline

count = 0
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

for i in T:
    left = 0
    right = n - 1
    found = False  
    while left <= right and not found:
        mid = (left + right) // 2
        if S[mid] == i:
            found = True  
        elif S[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
            
    if found:
        count += 1

print(count)









           




