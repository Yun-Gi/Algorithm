import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
f = 0 # 앞쪽 포인터
b = 0 # 뒤쪽 포인터
s = {}
counter = 0

while b < N:
    if lst[b] in s:
        s[lst[b]] += 1
    else:
        s[lst[b]] = 1
    while len(s) > 2:
        s[lst[f]] -= 1
        if s[lst[f]] == 0:
            del s[lst[f]]
        f += 1
    
    counter = max(counter, b - f + 1)
    b += 1

print(counter)
